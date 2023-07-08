"""Downloads all files from a connected badger / rpi pico to local directory."""
import logging
import pathlib

import ampy.files
import ampy.pyboard

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main(port: str, destination: pathlib.Path):
    board = ampy.pyboard.Pyboard(device=port)
    filesystem = ampy.files.Files(board)

    remote_files = filesystem.ls("/", long_format=False, recursive=True)
    remote_to_local_map = {
        fpath: pathlib.Path(destination / fpath[1:]) for fpath in remote_files
    }

    logger.info("Creating directories")
    for local_fpath in remote_to_local_map.values():
        local_fpath.parent.mkdir(parents=True, exist_ok=True)

    logger.info("Downloading files")
    for remote_fpath in remote_files:
        local_fpath = remote_to_local_map[remote_fpath]
        logger.debug("Downloading '%s' to '%s'", remote_fpath, local_fpath)
        content: bytes = filesystem.get(remote_fpath)
        local_fpath.write_bytes(content)


def parse_args(argv=None):
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=str, required=True)
    parser.add_argument(
        "--destination", default="./badger2040", type=pathlib.Path, required=False
    )
    parsed_args = parser.parse_args(argv)

    port = parsed_args.port
    destination = parsed_args.destination

    return port, destination


def cli():
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] %(levelname)-8s | %(name)s - %(message)s %(filename)s:%(lineno)d",
    )
    port, destination = parse_args()
    main(port, destination)


if __name__ == "__main__":
    cli()
