from cassandra.cluster import Cluster

# Connect to your Cassandra cluster
cluster_ips = ['127.0.0.1']  # Replace with your cluster IPs
cluster = Cluster(cluster_ips)
session = cluster.connect()

# Get all keyspaces
keyspaces = session.execute("SELECT keyspace_name FROM system_schema.keyspaces;")

# Drop each keyspace
for keyspace in keyspaces:
    keyspace_name = keyspace.keyspace_name
    if keyspace_name not in ['system', 'system_auth', 'system_distributed', 'system_schema', 'system_traces']:
        print(f"Dropping keyspace: {keyspace_name}")
        session.execute(f"DROP KEYSPACE {keyspace_name};")