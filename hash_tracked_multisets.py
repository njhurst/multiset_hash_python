from multiset_hash_python import PyRistrettoHash
import pickle

class HashTrackedSet(set):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hash = PyRistrettoHash()
        for item in self:
            self._add_to_hash(item)

    def _add_to_hash(self, item):
        self._hash.add(pickle.dumps(item), 1)

    def _remove_from_hash(self, item):
        self._hash.add(pickle.dumps(item), -1)

    def add(self, item):
        if item not in self:
            super().add(item)
            self._add_to_hash(item)

    def remove(self, item):
        super().remove(item)
        self._remove_from_hash(item)

    def discard(self, item):
        if item in self:
            super().discard(item)
            self._remove_from_hash(item)

    def pop(self):
        item = super().pop()
        self._remove_from_hash(item)
        return item

    def clear(self):
        for item in self:
            self._remove_from_hash(item)
        super().clear()

    def update(self, *others):
        for other in others:
            for item in other:
                if item not in self:
                    self._add_to_hash(item)
        super().update(*others)

    def get_hash(self):
        return self._hash.finalize()


class HashTrackedDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hash = PyRistrettoHash()
        for key, value in self.items():
            self._add_to_hash(key, value)

    def _add_to_hash(self, key, value):
        self._hash.add(pickle.dumps((key, value)), 1)

    def _remove_from_hash(self, key, value):
        self._hash.add(pickle.dumps((key, value)), -1)

    def __setitem__(self, key, value):
        if key in self:
            self._remove_from_hash(key, self[key])
        super().__setitem__(key, value)
        self._add_to_hash(key, value)

    def __delitem__(self, key):
        self._remove_from_hash(key, self[key])
        super().__delitem__(key)

    def pop(self, key, *args):
        if key in self:
            value = self[key]
            self._remove_from_hash(key, value)
        return super().pop(key, *args)

    def popitem(self):
        key, value = super().popitem()
        self._remove_from_hash(key, value)
        return key, value

    def clear(self):
        for key, value in self.items():
            self._remove_from_hash(key, value)
        super().clear()

    def update(self, *args, **kwargs):
        if args:
            other = args[0]
            if isinstance(other, dict):
                for key, value in other.items():
                    self.__setitem__(key, value)
            else:
                for key, value in other:
                    self.__setitem__(key, value)
        for key, value in kwargs.items():
            self.__setitem__(key, value)

    def get_hash(self):
        return self._hash.finalize()
    
if __name__ == "__main__":
    # Using HashTrackedSet
    s = HashTrackedSet([1, 2, 3])
    print("Initial set hash:", s.get_hash())

    s.add(4)
    print("After adding 4:", s.get_hash())

    s.remove(2)
    print("After removing 2:", s.get_hash())

    s.update([5, 6])
    print("After updating with [5, 6]:", s.get_hash())

    # Using HashTrackedDict
    d = HashTrackedDict({'a': 1, 'b': 2})
    print("\nInitial dict hash:", d.get_hash())

    d['c'] = 3
    print("After adding 'c': 3:", d.get_hash())

    del d['a']
    print("After deleting 'a':", d.get_hash())

    d.update({'d': 4, 'e': 5})
    print("After updating with {'d': 4, 'e': 5}:", d.get_hash())