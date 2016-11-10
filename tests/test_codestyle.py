import pycodestyle


def test_conformance():
    """Test that we conform to PEP-8."""
    style = pycodestyle.StyleGuide(quiet=False,
        config_file='setup.cfg')
    style.input_dir('wishfulsc2')
    style.input_dir('tests')
    result = style.check_files()
    assert result.total_errors == 0, "Found code style errors (and warnings)."
