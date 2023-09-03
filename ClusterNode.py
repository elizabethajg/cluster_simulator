'''
### Cluster Node Representation
A class representing a cluster node will be used for the simulation. 
Properties to include:
* Node ID
* Status (online/offline)
* Failure recovery time (seconds required between initiating recovery and succesful reintegration for this node) 
Functions to include:
* Get/set properties
* on_failure
* recover
'''
import time
class ClusterNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.status = 'offline'
        self.recovery_time = 5
        self.failure_history = []
    
    def __init__(self, node_id, recovery_time):
        self.node_id = node_id
        self.status = 'offline'
        self.recovery_time = recovery_time
        self.failure_history = []

    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status = status

    def get_recovery_time(self):
        return self.recovery_time
    def set_recovery_time(self, recovery_time):
        self.recovery_time = recovery_time

    def get_id(self):
        return self.node_id
    def set_id(self, node_id):
        self.node_id = node_id

    def get_failure_history(self):
        return self.failure_history
    # Set method for failure history is intended for implementation of redundancy nodes
    # Not for updating failure history list
    def set_failure_history(self, failure_history):
        self.failure_history = failure_history

    #TODO: implement on_failure function
    def on_failure():
        return
    
    #TODO: implement recover function
    def recover():
        return