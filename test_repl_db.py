import unittest
from repl_db import ReplicatedDatabase

class TestReplicatedDatabase(unittest.TestCase):
    def test_add_replica(self):
        # Создаем базу данных и реплику
        primary_db = ReplicatedDatabase("Primary DB")
        replica_db = ReplicatedDatabase("Replica DB")
        
        # Добавляем реплику к основной базе данных
        primary_db.add_replica(replica_db)
        
        # Проверяем была ли добавлена реплика в список
        self.assertIn(replica_db, primary_db.replicas)
        
    def test_add_data(self):
        # Создаем базу данных и реплику
        primary_db = ReplicatedDatabase("Primary DB")
        replica_db = ReplicatedDatabase("Replica DB")
        
        # Добавляем реплику к основной базе данных
        primary_db.add_replica(replica_db)
        
        # Добавляем данные в основную базу
        primary_db.add_data("key1", "value1")
        
        # Проверяем были ли добавлены данные в базу
        self.assertEqual(primary_db.data, {"key1": "value1"})
        
        # Проверяем были ли добавлены данные в реплику
        self.assertEqual(replica_db.data, {"key1": "value1"})
        
    def test_multiple_replicas(self):
        # Создаем базу данных и две реплики
        primary_db = ReplicatedDatabase("Primary DB")
        replica_db1 = ReplicatedDatabase("Replica DB 1")
        replica_db2 = ReplicatedDatabase("Replica DB 2")
        
        # Добавляем обе реплики к основной базе 
        primary_db.add_replica(replica_db1)
        primary_db.add_replica(replica_db2)
        
        # Добавляем данные в основную базу
        primary_db.add_data("key1", "value1")
        
        # Проверяем были ли дублированы данные в реплики
        self.assertEqual(replica_db1.data, {"key1": "value1"})
        self.assertEqual(replica_db2.data, {"key1": "value1"})

if __name__ == "__main__":
    unittest.main()
