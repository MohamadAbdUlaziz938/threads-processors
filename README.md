## Multithreading vs. Multiprocessing
By formal definition, multithreading refers to the ability of a processor to execute multiple threads concurrently, where each thread runs a process. Whereas multiprocessing refers to the ability of a system to run multiple processors concurrently, where each processor can run one or more threads.
<a href="#screenshots">
<img src="https://github.com/MohamadAbdUlaziz938/interval-time-selector/blob/master/screenshots/1.png" width="200px">
</a>
From the diagram above, we can see that in multithreading (middle diagram), multiple threads share the same code, data, and files but run on a different register and stack. Multiprocessing (right diagram) multiplies a single processor — replicating the code, data, and files, which incurs more overhead.

Multithreading is useful for IO-bound processes, such as reading files from a network or database since each thread can run the IO-bound process concurrently. Multiprocessing is useful for CPU-bound processes, such as computationally heavy tasks since it will benefit from having multiple processors; similar to how multicore computers work faster than computers with a single core.

## Note
"Note that using multithreading for CPU-bound processes might slow down performance due to competing resources that ensure only one thread can execute at a time, and overhead is incurred in dealing with multiple threads."

On the other hand, multiprocessing can be used for IO-bound processes. However, overhead for managing multiple processes is higher than managing multiple threads as illustrated above. You may notice that multiprocessing might lead to higher CPU utilization due to multiple CPU cores being used by the program, which is expected.