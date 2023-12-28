def test_import_module():
    import minimum_python

    assert minimum_python is not None
    assert minimum_python.__version__ == "0.0.1"
