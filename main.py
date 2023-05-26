from pathlib import Path

from src.compress import compress_multiple_files
from src.decompress import decompress
from src.parse_args import parse_arguments


def main(root_dir: Path):
    args = parse_arguments()



    if args.mode == 'compress':
        destination = root_dir
        compress_multiple_files(destination, args.files)
    elif args.mode == 'decompress':
        decompress(args.file)


if __name__ == '__main__':
    root_dir = Path.cwd()
    main()
