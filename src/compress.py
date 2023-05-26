import tarfile
from pathlib import Path
from typing import List


def compress_one_file(input_file: Path, destination_tarball: Path):
    with tarfile.open(destination_tarball, "w:gz") as tar:
        tar.add(input_file, arcname=input_file.name)


def compress_multiple_files(destination_tarball: Path, input_files: List[Path]):
    with tarfile.open(destination_tarball, "w:gz") as tar:
        for input_file in input_files:
            tar.add(input_file, arcname=input_file.name)
