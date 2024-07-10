# Multiset Hash

Multiset Hash is a Rust/Maturin library that provides a commutative hash function for multi-sets. It's built on top of the Ristretto group and uses the SHA512 hash function, offering a unique combination of performance and cryptographic properties.

## Features

- Commutative hashing: The order of adding elements doesn't affect the final hash.
- Support for multiplicities: Elements can be added or removed multiple times efficiently.
- Incremental updates: Hash can be updated in parts, allowing for streaming or chunked data processing.
- Cryptographically secure: Based on the Ristretto group and SHA512 hash function.
- Python bindings: Easy to use in Python projects while leveraging Rust's performance.

## Installation

To install Multiset Hash, you need to have Rust and Python installed on your system. Then you can install it using pip:

```bash
pip install maturin
maturin develop
```

## TODOs
 - work out how to package and install from PyPI
 - switch to BLAKE3 (issues: only 256b by default, couldn't work out all the Traits stuff)

## Usage

Here's a simple example of how to use Multiset Hash:

```python
from multiset_hash_python import PyRistrettoHash

# Create a new hash object
hash = PyRistrettoHash()

# Add some data
hash.add(b"apple", 3)  # Add "apple" three times
hash.add(b"banana", 2)  # Add "banana" twice

# Remove an item
hash.add(b"apple", -1)  # Remove one "apple"

# Add data in parts
hash.update(b"oran")
hash.update(b"ge")
hash.end_update(1)  # Finish adding "orange" once

# Finalize and get the hash
result = hash.finalize()
print(result.hex())
```

## API Reference

### `PyRistrettoHash`

#### `__init__()`
Creates a new PyRistrettoHash object.

#### `add(data: bytes, multiplicity: int)`
Adds `data` to the hash `multiplicity` times. Use negative values for `multiplicity` to remove items.

#### `update(data: bytes)`
Updates the hash with a part of an object. Must be followed by `end_update()`.

#### `end_update(multiplicity: int)`
Finalizes a partial update started with `update()`.

#### `finalize() -> bytes`
Finalizes the hash computation and returns the hash value as bytes.

## Development

To set up the development environment:

1. Clone the repository
2. Install Rust (https://www.rust-lang.org/tools/install)
3. Install Maturin: `pip install maturin`
4. Build the project: `maturin develop`

To run tests:

```bash
python tests/test_multiset_hash.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project is based on the [multiset-hash](https://github.com/cronokirby/multiset-hash) crate but modified to allow negative multiplicities (https://github.com/njhurst/multiset-hash).
- Uses the [curve25519-dalek](https://github.com/dalek-cryptography/curve25519-dalek) library for Ristretto group operations.
- Uses [SHA512] for hashing.