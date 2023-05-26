from pathlib import Path

from src.compress import compress_multiple_files
from src.decompress import decompress
from src.parse_args import parse_arguments
from src.ui.main import TarManApp


if __name__ == '__main__':
    root_dir = Path.cwd()
    args = parse_arguments()

    debug_gui = True

    if debug_gui:
        app = TarManApp()
        app.run()

    if args.mode == 'compress':
        destination = root_dir
        compress_multiple_files(destination, args.files)

    elif args.mode == 'decompress':
        chosen_file_path = Path(args.file)
        tarball_path = chosen_file_path
        destination = chosen_file_path.cwd() / chosen_file_path.stem.split(".")[0]
        decompress(destination, tarball_path)
