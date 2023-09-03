## Overview: 
Create a simplified high-availability cluster system simulator using python.

### Defintions:
* Cluster: A group of nodes that work together to keep a server running effectively. Advantages include fault tolerance, flexible load bearing configurations, and scalability. 
* High-availability: Refers to the systems ability to operate with minimal downtime. Features of a high-availabilty system may include:
    * Redundancies and failovers: Backup components are configured such that if a component fails, the traffic is diverted to the failover. The backup enables the system to handle component failure without human intervention.
    * Automated system monitoring: A cluster controller equipped with automated monitering is responsible for monitoring nodes, initiating failure procedures, distributing server traffic among nodes, and providing adminstrators with alerts and updates.


## Motivation:
* Prepare some code to present at Iris Analytics interview that is explicitly relevant to the job.
* Gain a deeper understanding of clusters and related operations.
* Practice some python.
* Demonstrate competency in all four pillars of OOP.

## Features:

### Cluster Node Representation
A class representing a cluster node will be used for the simulation. 
Properties to include:
* Node ID
* Status (online/offline)
* Failure recovery time (seconds required between initiating recovery and succesful reintegration for this node) 
Functions to include:
* Get/set properties

### Cluster Controller
A class containing procedures that monitor and manage cluster nodes. 
Properties to include:
* Nodes
* Failure log

Functions to include:
* Initialize cluster
* Add/remove node
* Check node status
* Recover node
* Reintegrate node
* Status report

### Simulation
A class that contains functions to randomly generate node failures to be detected by the controller. 
Properties to include:
* Failure rate (average number of failures / 60 seconds)
* Runtime (in seconds)
Functions to include:
* Initialize
* Reset/restart

Functions to include:
* Get/set properties
* Start simulation
* Trigger failure
* Set failure rate
* End simulation

### Node failure
A class that stores information about each node failure.
Properties:
* Node
* Time of failure
* Recovered at
* Downtime

Functions:
* Initialize
* Get/set properties
