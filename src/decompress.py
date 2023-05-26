import tarfile
from pathlib import Path


class NotATarFileError(Exception):
    """ Raised when the file is expected to be a tar.gz file, but it is not """
    pass

    default_message = "Selected file is not an archive file. Please select a valid tarfile for extraction."


def decompress(destination: Path, input_tarball: Path):
    if not tarfile.is_tarfile(input_tarball):
        print(f"{input_tarball} is not a tar file.")
        raise NotATarFileError(NotATarFileError.default_message)

    file_obj = tarfile.open(input_tarball, "r")
    # namelist = file_obj.getnames()
    file_obj.extractall(destination)
    file_obj.close()
