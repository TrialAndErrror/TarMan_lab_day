from pathlib import Path

import pytest

from src.compress import compress_one_file, compress_multiple_files
from src.decompress import decompress


@pytest.fixture
def input_files(tmp_path):
    # Create multiple temporary input files for testing
    for num in range(10):
        input_file_path = tmp_path / f'input_{num}.txt'
        with open(input_file_path, 'w') as f:
            f.write(f'This is a test file. #{num}')
    return tmp_path.glob('*.txt')


@pytest.fixture
def output_tarball(tmp_path):
    # Create a temporary output tarball for testing
    return tmp_path / 'output.tar.gz'


def test_compress_and_decompress(input_files, output_tarball):
    output_dir = Path.cwd() / "test_output_files"
    output_dir.mkdir(exist_ok=True)

    destination_file = output_dir / "output.tar.gz"
    # Compress the input file into the tarball
    compress_multiple_files(destination_file, input_files)

    # Ensure the tarball exists
    assert destination_file.exists()

    # Decompress the tarball into a temporary output file
    output_file_dir = output_tarball.cwd() / output_tarball.stem
    output_file_dir.mkdir(exist_ok=True, parents=True)

    decompress(destination_file, output_file_dir)

    # Ensure the output file exists
    for num in range(10):
        output_file = output_file_dir / f'input_{num}.txt'
        assert output_file.exists()

    # Verify the content of the output file
        with open(output_file, 'r') as f:
            assert f.read() == f'This is a test file. #{num}'

    # Clean up temporary files
        output_file.unlink()
        assert not output_file.exists()


    destination_file.unlink()
    output_file_dir.rmdir()
    output_dir.rmdir()

    # Ensure the temporary files are deleted
    assert not output_tarball.exists()
    assert not output_file_dir.exists()
    assert not output_dir.exists()