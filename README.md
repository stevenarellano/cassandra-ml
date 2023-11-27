# official cassandra here
https://github.com/apache/cassandra


# important to run before running db (versioning)
export JAVA_HOME=`/usr/libexec/java_home -v 1.8`


# run the db
bin/cassandra -f


# run cql
bin/cqlsh


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

For each cassandra.yaml
data_file_directories: add /cassandra(x)/ to path
commitlog_directory: add /cassandra(x)/ to path
saved_caches_directory: add /cassandra(x)/ to path
listen_address: 127.0.0.x
rpc_address: 127.0.0.x


For each Cassandra-env.sh
JMX port: change to unique port #

Make X copies of cassandra.in.sh and cassadra in the bin folder
1. Change the path to conf in cassandra.in.sh

Run
sudo ifconfig lo0 alias 127.0.0.2
