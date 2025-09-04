use numpy::{PyArray1, PyReadonlyArray1};
use pyo3::prelude::*;

#[pyfunction]
fn double_array(py: Python<'_>, input: PyReadonlyArray1<'_, f64>) -> PyResult<()> {
    let array = input.as_array();

    // Iterate over each element with coordinates
    for (i, value) in array.indexed_iter() {
        println!("Element at ({}) = {}", i, value);
    }
    Ok(())
}

#[pymodule]
fn nprandom(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(double_array, m)?)?;
    Ok(())
}