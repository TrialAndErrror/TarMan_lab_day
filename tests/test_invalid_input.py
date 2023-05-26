from pathlib import Path
import pytest
from src.decompress import NotATarFileError, decompress


@pytest.fixture
def not_a_tar_file(tmp_path):
    file_path = Path(tmp_path / 'input.txt')
    file_path.touch(exist_ok=True)
    return file_path


def test_decompress_not_an_archive(not_a_tar_file):
    output_dir = Path.cwd() / "test_output_files"
    output_dir.mkdir(exist_ok=True)

    # Try to decompress the tarball into a temporary output file
    with pytest.raises(NotATarFileError, match=NotATarFileError.default_message):
        decompress(output_dir, not_a_tar_file)

    # Ensure the output file exists
    output_file = output_dir / 'input.txt'
    assert not output_file.exists()

    output_dir.rmdir()
    assert not output_dir.exists()
