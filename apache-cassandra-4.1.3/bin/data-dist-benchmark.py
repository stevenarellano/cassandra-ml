import csv
import time
from cassandra.cluster import Cluster
import uuid
import subprocess

# Configuration
keyspace = 'benchmark_keyspace'
table = 'benchmark_table'
num_operations = 25000  # Updated number of read/write operations
monitoring_interval = 250  # Updated monitoring interval
output_file = 'node_distribution_over_time.csv'

# Connect to the Cassandra cluster
cluster_ips = ['127.0.0.1']  # Replace with your cluster IPs
cluster = Cluster(cluster_ips)
session = cluster.connect()

# Create keyspace and table


def setup_schema():
    session.execute(
        f"CREATE KEYSPACE IF NOT EXISTS {keyspace} WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': '1'}};")
    session.execute(f"USE {keyspace};")
    session.execute(
        f"CREATE TABLE IF NOT EXISTS {table} (id UUID PRIMARY KEY, value text);")


def write_data():
    try:
        query = session.prepare(
            f"INSERT INTO {table} (id, value) VALUES (?, ?)")
        session.execute(
            query, (uuid.uuid4(), 'Some data ' + str(uuid.uuid4())))
    except Exception as e:
        print(f"Error in write operation: {e}")

# Perform read operation


def read_data():
    try:
        query = session.prepare(f"SELECT * FROM {table} WHERE id = ?")
        session.execute(query, (uuid.uuid4(),))
    except Exception as e:
        print(f"Error in read operation: {e}")


# Function to get node load information
def get_node_flush():
    try:
        subprocess.call(["./nodetool", "flush"])
        output = subprocess.check_output(
            ["./nodetool", "status"]).decode("utf-8")
        lines = output.split('\n')
        node_data = []
        for line in lines:
            # 'UN' for Up/Normal, 'DN' for Down/Normal
            if line.startswith('UN') or line.startswith('DN'):
                parts = line.split()
                node_info = {
                    'status': parts[0],  # UN or DN
                    'address': parts[1],  # IP address
                    'load': parts[2] + " " + parts[3],  # Data load with unit
                    'tokens': int(parts[4]),  # Number of tokens
                    'owns': parts[5],  # Percentage of data owned
                    'host_id': parts[6],  # Host ID
                    'rack': parts[7]  # Rack information
                }
                node_data.append(node_info)
        return node_data
    except subprocess.CalledProcessError as e:
        print(f"Error executing nodetool status: {e}")
        return []


# Function to get real-time data distribution across nodes
def get_realtime_data_distribution():
    try:
        return get_node_flush()
    except Exception as e:
        print(f"Error fetching data distribution: {e}")
        return []

# Store results to a CSV file


def store_results(data):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['operation_count', 'data_distribution'])
        for row in data:
            writer.writerow(row)

# Main benchmarking function


def run_benchmark():
    results = []
    for i in range(num_operations):
        if i % 2 == 0:
            write_data()
        else:
            read_data()

        if (i + 1) % monitoring_interval == 0:
            data_distribution = get_realtime_data_distribution()
            print(i,str(data_distribution))
            results.append([i + 1, str(data_distribution)])

    return results


# Run the script
setup_schema()
benchmark_data = run_benchmark()
store_results(benchmark_data)
