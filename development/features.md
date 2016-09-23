---
title: Features in progress and to be developed
---

SpiNNaker Software development uses (loosely) a Functionally Driven Development methodology.  As such, we have a set of features that we are working on at present or that work is planned to start on in the future.  The titles below give a brief overview of these features.  Each feature is then linked with the appropriate issues and pull requests that give more detail about the feature.  

Note that in some cases, there will be no pull requests or issues; this indicates that we recognise a feature in need of software engineering effort but have not yet thought about the details.

# [Low-level interface to tools](https://github.com/issues?q=is%3Aopen+user%3ASpiNNakerManchester+milestone:low-level-interface)
This will provide a low-level interface to complete the integration of rig into the tools.  This includes the ability to run a "place-and-route" in a single operation from a machine graph, the ability to write data in a "file-like" way (including seeks), and the ability to load executables and data in a single call to the machine.  This will also include some changes so that software features can be used in isolation of other features e.g. recording when data specification generation has not been used.

# [Improved Multi-board support](https://github.com/issues?q=is%3Aopen+user%3ASpiNNakerManchester+milestone:multi-board)
This will improve the support for using multiple boards, both through changes to SpiNNMan and through improved support for live input and output when multiple Ethernet-connected-chips are present.

# [Fix External Device support](https://github.com/issues?q=is%3Aopen+user%3ASpiNNakerManchester+milestone:external-device)
Support for external devices is currently broken - the sending of commands to the device in particular needs to be fixed.

# [Complete PyNN 0.7 support](https://github.com/issues?q=is%3Aopen+user%3ASpiNNakerManchester+milestone:pynn-0.7)
The software will be updated to include the complete set of PyNN 0.7 features where feasible.

# [PyNN 0.8 support](https://github.com/issues?q=is%3Aopen+user%3ASpiNNakerManchester+milestone:pynn-0.8)
The software will be updated to include the complete set of PyNN 0.8 features.  This may be implemented in a new module.

# [Improved Delay representation](https://github.com/issues?q=is%3Aopen+user%3ASpiNNakerManchester+milestone:delay-representation)
Delays in sPyNNaker are currently require a delay extension.  Another linked-list representation would remove this need, at the cost of needing more DMAs to be executed.

# [Improved Loading speed](https://github.com/issues?q=is%3Aopen+user%3ASpiNNakerManchester+milestone:faster-loading)
Synaptic matrices are currently expanded on host and then loaded.  Instead, the matrix should be expanded on the machine where possible.

# [Improve reliability of the HBP service](https://github.com/issues?q=is%3Aopen+user%3ASpiNNakerManchester+milestone:reliable-hbp-service)
The HBP service should be able to cope with events such as the central NMPI server being unavailable or the service being restarted whilst jobs are running.

# [New External Device Protocol](https://github.com/issues?q=is%3Aopen+user%3ASpiNNakerManchester+milestone:eieio-v2)
The current version of EIEIO doesn't support features such as packets with both time, keys and payloads.  Development of a new version of EIEIO is in progress.  Additionally, this should be linked to the MUSIC protocol to ensure that SpiNNaker software can communicate with other devices.

# [Change Poisson rates during simulation](https://github.com/issues?q=is%3Aopen+user%3ASpiNNakerManchester+milestone:dynamic-poisson)
It is currently only possible to specify the Poisson rate once for a whole simulation.  Instead it would be good to support multiple rates throughout the simulation e.g. as a list with start and end times (non-overlapping).

# [Allocate ports dynamically](https://github.com/issues?q=is%3Aopen+user%3ASpiNNakerManchester+milestone:dynamic-ports)
Where IP tags are used, a socket should be opened first after which the port number of the socket can then be requested in the tag, rather than using a fixed port number.  The database should then also allow dynamic registration of externally listening receivers of IP tag traffic.

# [Work out CPU and DTCM usage](https://github.com/issues?q=is%3Aopen+user%3ASpiNNakerManchester+milestone:profiling)
Each of the components should be profiled in terms of the CPU and DTCM usage to make more accurate decisions about partitioning.  A profiler is in progress to aid in this work.

# [Partitioning, Placement and Routing Algorithms](https://github.com/issues?q=is%3Aopen+user%3ASpiNNakerManchester+milestone:place-and-route)
Improvements to the Partitioning, Placement and Routing to aid in the mapping of problems on to the machine.  This should include bringing rig algorithms into PACMAN.

# [Testing](https://github.com/issues?q=is%3Aopen+user%3ASpiNNakerManchester+milestone:testing)
Currently integration tests are based on looking at the outputs.  The few unit tests in existence are mostly broken.  Thus the automated tests almost always fail.  The integration tests should be made to be like unit tests, and unless absolutely necessary, the unit tests should be removed; instead feature tests should be developed to ensure that the features work as expected.

# [Database on SpiNNaker](https://github.com/issues?q=is%3Aopen+user%3ASpiNNakerManchester+milestone:database-on-spinnaker)
The implementation of a Database application using SpiNNaker.

# [Split Neural Models](https://github.com/issues?q=is%3Aopen+user%3ASpiNNakerManchester+milestone:split-neural-model)
This will split the neural and synapse models so that they are run on separate cores.  This has several advantages, including the ability to run at 0.1ms in real-time and the ability to have multiple STDP rules on a single connection between two populations of neurons.
