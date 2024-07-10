import unittest
from multiset_hash_python import PyRistrettoHash

class TestPyRistrettoHash(unittest.TestCase):
    def test_add_with_multiplicity(self):
        data = b"test data"

        hash1 = PyRistrettoHash()
        hash2 = PyRistrettoHash()

        hash1.add(data, 3)
        hash2.add(data, 1)
        hash2.add(data, 1)
        hash2.add(data, 1)

        self.assertEqual(hash1.finalize(), hash2.finalize())

    def test_add_and_sub_with_multiplicity(self):
        data = b"test data"

        hash1 = PyRistrettoHash()
        hash2 = PyRistrettoHash()

        hash1.add(data, 1)
        hash2.add(data, 1)
        hash2.add(data, 1)
        hash2.add(data, -1)

        self.assertEqual(hash1.finalize(), hash2.finalize())

    def test_hash_commutative(self):
        data_a = b"test data A"
        data_b = b"test data B"

        hash1 = PyRistrettoHash()
        hash2 = PyRistrettoHash()

        hash1.add(data_a, 1)
        hash1.add(data_b, 1)

        hash2.add(data_b, 1)
        hash2.add(data_a, 1)

        self.assertEqual(hash1.finalize(), hash2.finalize())

    def test_partial_updates(self):
        hash1 = PyRistrettoHash()
        hash2 = PyRistrettoHash()

        hash1.add(b"the full data", 3)
        
        hash2.update(b"the")
        hash2.update(b" full")
        hash2.update(b" data")
        hash2.end_update(3)

        self.assertEqual(hash1.finalize(), hash2.finalize())

    def test_remove_items(self):
        hash1 = PyRistrettoHash()
        hash2 = PyRistrettoHash()

        hash1.add(b"item", 5)
        hash1.add(b"item", -2)

        hash2.add(b"item", 3)

        self.assertEqual(hash1.finalize(), hash2.finalize())

if __name__ == '__main__':
    unittest.main()