# Fork of Cassandra-DB

### What

- implmented the folloiwng 3 new paritioning algorithms for Cassandra-DB

1. XXHash
2. CityHash
3. Blake3

### Methodology

Partitioner Implementation: Custom partitioner classes for XXHash, CityHash, and Blake3 were created and integrated into a cloned Cassandra environment.
Benchmarking Setup: The experiment was conducted on both local and cloud (AWS EC2 instances) setups, allowing for comprehensive testing conditions.

### Evaluation Metrics

Collision Resistance: Measured by the number of key collisions per 1 million keys.
Node Distribution: Assessed by the percentage of data distribution across nodes, particularly focusing on hotspot reduction.
Performance/Latency: Evaluated through read/write operation timings and overall system throughput.

### Results

#### Collision Resistance

Murmur3: 144.64 collisions per 1M keys
XXHash: 185.23 collisions per 1M keys
CityHash: 44.88 collisions per 1M keys

#### Load Distribution

Murmur3: Hotspot ~47% at 25,000 operations
XXHash: Hotspot ~50% at 25,000 operations
CityHash: Hotspot ~36% at 25,000 operations

#### Latency

Murmur3: Write benchmark at 24,172 ops/sec with a mean response time of 5.065 ms; Read benchmark at 17,418 ops/sec with a mean response time of 7.079 ms.
XXHash: Write benchmark at 7,775 ops/sec with a mean response time of 15.996 ms; Read benchmark at 5,317 ops/sec with a mean response time of 23.660 ms.
CityHash: Write benchmark at 7,915 ops/sec with a mean response time of 15.635 ms; Read benchmark at 5,969 ops/sec with a mean response time of 21.051 ms.
