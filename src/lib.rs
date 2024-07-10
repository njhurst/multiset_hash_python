use pyo3::prelude::*;
use multiset_hash::RistrettoHash;
use sha2::Sha512;

use digest::Digest;

#[pyclass]
struct PyRistrettoHash {
    inner: RistrettoHash<Sha512>,
}

#[pymethods]
impl PyRistrettoHash {
    #[new]
    fn new() -> Self {
        PyRistrettoHash {
            inner: RistrettoHash::<Sha512>::default(),
        }
    }

    fn add(&mut self, data: &[u8], multiplicity: i64) {
        self.inner.add(data, multiplicity);
    }

    fn update(&mut self, data: &[u8]) {
        self.inner.update(data);
    }

    fn end_update(&mut self, multiplicity: i64) {
        self.inner.end_update(multiplicity);
    }

    fn finalize(&mut self) -> Vec<u8> {
        <RistrettoHash<Sha512> as Clone>::clone(&self.inner).finalize().to_vec()
    }
}

#[pymodule]
fn multiset_hash_python(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<PyRistrettoHash>()?;
    Ok(())
}