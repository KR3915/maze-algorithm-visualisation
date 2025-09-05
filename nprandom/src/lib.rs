use numpy::{PyArray2, PyReadonlyArray2};
use pyo3::prelude::*;
use rand::Rng;

#[pyfunction]
fn randomize(py: Python<'_>, input: PyReadonlyArray2<'_, f64>, density: f64) -> PyResult<Py<PyArray2<i32>>> {
    let array = input.as_array();
    let shape = array.shape();
    let mut rng = rand::rng();

    // Create a new 2D Vec to store the output
    let mut output = vec![vec![0i32; shape[1]]; shape[0]];

    for ((i, j), _value) in array.indexed_iter() {
        let rand_num = rng.random_range(1..100);
        output[i][j] = if rand_num < (density) as i32 { 1 } else { 0 };
    }

    // Convert Vec<Vec<i32>> to PyArray2<i32> and return it
    let pyarray = PyArray2::from_vec2(py, &output).unwrap();
    Ok(pyarray.to_owned().into())
}

#[pymodule]
fn maze(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(randomize, m)?)?;
    Ok(())
}