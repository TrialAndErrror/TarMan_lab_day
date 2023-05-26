import tarfile
from pathlib import Path


def compress_one_file(input_file: Path, destination_tarball: Path):
    with tarfile.open(destination_tarball, "w:gz") as tar:
        tar.add(input_file, arcname=input_file.name)
