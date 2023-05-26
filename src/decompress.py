import tarfile
from pathlib import Path


def decompress(input_tarball: Path, output_filepath: Path):
    if not tarfile.is_tarfile(input_tarball):
        print(f"{input_tarball} is not a tar file.")
        return

    file_obj = tarfile.open(input_tarball, "r")
    namelist = file_obj.getnames()
    file_obj.extractall(output_filepath)
    file_obj.close()
