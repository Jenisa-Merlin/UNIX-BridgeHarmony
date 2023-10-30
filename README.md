# UNIX-BridgeHarmony
Single Lane Bridge Problem


Introduction:
	The Single Lane Bridge Problem presents a scenario where a bridge connecting two villages becomes a potential deadlock point for farmers traveling in opposite directions. This project tackles this problem by employing POSIX synchronization techniques, including mutex locks and semaphores. The objective is to ensure safe passage for farmers from North Tunnel and South Tunnel, preventing any possible deadlock situations.

Problem Statement:
A single-lane bridge connects two villages of North Tunbridge and South Tunbridge. Farmers in the two villages use this bridge to deliver their produce to the neighboring town. The bridge can become deadlocked if a northbound and a southbound farmer get on the bridge at the same time. (The farmers are stubborn and are unable to back up. 

Methodology/Approach:
To address the Single Lane Bridge Problem, POSIX synchronization mechanisms, specifically mutex locks and semaphores, were employed. Mutex locks were used to control access to critical sections of code, ensuring exclusive access to the bridge. Semaphores were employed to regulate the number of farmers allowed on the bridge at any given time, preventing conflicts between northbound and southbound travellers.
Additionally, a randomized sleep period was incorporated to simulate the time taken by farmers to traverse the bridge. This added a dynamic element to the simulation, enhancing realism.

Findings:
The implementation of the proposed algorithm successfully mitigated the deadlock scenario on the single-lane bridge. Extensive testing under various scenarios demonstrated the robustness and effectiveness of the solution. The use of mutex locks and semaphores provided a reliable means of synchronization, ensuring safe passage for farmers from both villages.

Conclusion/Impact:
This project demonstrates the effectiveness of POSIX synchronization techniques in resolving real-world concurrency issues. The implemented solution showcases the importance of proper synchronization mechanisms in multi-threaded environments. The findings from this project can be extended to similar scenarios, to ensure the integrity of critical operations.

