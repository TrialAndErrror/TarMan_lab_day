from pathlib import Path

import pytest

from src.compress import compress_multiple_files
from src.decompress import decompress


@pytest.fixture
def input_file(tmp_path):
    # Create a temporary input file for testing
    input_file_path = tmp_path / 'input.txt'
    with open(input_file_path, 'w') as f:
        f.write('This is a test file.')
    return input_file_path


@pytest.fixture
def output_tarball(tmp_path):
    # Create a temporary output tarball for testing
    return tmp_path / 'output.tar.gz'


def test_compress_and_decompress(input_file, output_tarball):
    output_dir = Path.cwd() / "test_output_files"
    output_dir.mkdir(exist_ok=True)

    destination_file = output_dir / "output.tar.gz"
    # Compress the input file into the tarball
    compress_multiple_files(destination_file, [input_file, ])

    # Ensure the tarball exists
    assert destination_file.exists()

    # Decompress the tarball into a temporary output file
    output_file_dir = output_tarball.cwd() / output_tarball.stem
    output_file_dir.mkdir(exist_ok=True, parents=True)

    decompress(destination_file, output_file_dir)

    # Ensure the output file exists
    output_file = output_file_dir / 'input.txt'
    assert output_file.exists()

    # Verify the content of the output file
    with open(output_file, 'r') as f:
        assert f.read() == 'This is a test file.'

    # Clean up temporary files
    output_file.unlink()
    destination_file.unlink()
    output_file_dir.rmdir()

    # Ensure the temporary files are deleted
    assert not output_file.exists()
    assert not output_tarball.exists()
    assert not output_file_dir.exists()
