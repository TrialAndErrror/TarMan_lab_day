import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='File compression and decompression utility')

    subparsers = parser.add_subparsers(dest='mode', help='Choose mode: compress or decompress')

    # Compression mode
    compress_parser = subparsers.add_parser('compress', help='Compress files')
    compress_parser.add_argument('files', nargs='+', help='Files to compress')

    # Decompression mode
    decompress_parser = subparsers.add_parser('decompress', help='Decompress a file')
    decompress_parser.add_argument('file', help='File to decompress')

    return parser.parse_args()


