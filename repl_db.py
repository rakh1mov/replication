class ReplicatedDatabase:
    def __init__(self, name):
        self.name = name
        self.data = {}
        self.replicas = []
        
    def add_replica(self, replica_database):
        """
        добавляем реплики 
        """
        self.replicas.append(replica_database)
        
    def add_data(self, key, value):
        """
        добавляем данные в основную базу и реплики
        """
        self.data[key] = value
        for replica in self.replicas:
            replica.add_data(key, value)