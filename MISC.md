# official cassandra here

https://github.com/apache/cassandra

# running on mac (use homebrew)

brew install openjdk@11
export JAVA_HOME=/usr/local/opt/openjdk@11

# to build

ant -Drat.skip=true

# to run (mac)

1. cd cassandra-ml/apache-cassandra-4.1.3/bin
2. export JAVA_HOME=`/usr/libexec/java_home -v 1.8`
3. sudo ifconfig lo0 alias 127.0.0.2 (if needed)
4. ./cassandra -f

# run cql

1. cd cassandra-ml/apache-cassandra-4.1.3/bin
2. ./cqlsh

# random useful commands

- while in bin
  ./nodetool -h localhost -p 7199 status
  ./nodetool status

- find a process on a port & kill
  Find:
  sudo lsof -i :<PORT>
  Kill:
  kill -9 <PID>

### setting up a new node (local on same machine)

change the following

- For each cassandra.yaml in conf(x)

        * data_file_directories: add /cassandra(x)/ to path

```
data_file_directories:
    - $CASSANDRA_HOME/cassandra/data
```

        * commitlog_directory: add /cassandra(x)/ to path

```
commitlog_directory: $CASSANDRA_HOME/cassandra/commitlog
```

        * saved_caches_directory: add /cassandra(x)/ to path

```
saved_caches_directory: $CASSANDRA_HOME/cassandra/saved_caches
```

        * listen_address: 127.0.0.x
        * rpc_address: 127.0.0.x

- For each Cassandra-env.sh in conf(x)

  - JMX port: change to unique port #

- Make X copies of cassandra.in.sh and cassadra in the bin folder

for each cassandra.in.sh \* Change the path to conf in cassandra.in.sh

Run
_ sudo ifconfig lo0 alias 127.0.0.x
_ e.g. sudo ifconfig lo0 alias 127.0.0.2 \* e.g. sudo ifconfig lo0 alias 127.0.0.3

# running the benchmark

0. CLEAR DATABASE; MAKE SURE DATABASE IS RUNNING LOCALLY; RUN THE BELOW; WORKLOAD FILES ARE LOCATED AT /latte/workloads/\*.rn

1. latte schema <workload.rn> [<node address>] # create the database schema
2. latte load <workload.rn> [<node address>] # populate the database with data
3. latte run <workload.rn> [-f <function>] [<node address>] # execute the workload and measure the performance # YOU DON"T NEED TO DO THE ADDRESS (default is localhost)

# current partitioners

- Murmur3Partitioner (default): uniformly distributes data across the cluster based on MurmurHash hash values.
- RandomPartitioner: uniformly distributes data across the cluster based on MD5 hash values.
- ByteOrderedPartitioner: keeps an ordered distribution of data lexically by key bytes

# cool

pkill -f 'java.\*cassandra'

# reset all data

for each node
sudo rm -rf bin/$CASSANDRA_HOME

what this is doing:
sudo rm -rf /var/lib/cassandra/data/_
sudo rm -rf /var/lib/cassandra/commitlog/_
sudo rm -rf /var/lib/cassandra/saved_caches/\*
