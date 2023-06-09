import os
import sys
import json
import shutil
import logging
import argparse

sys.path.insert(0, "./devgoldyutils")

from devgoldyutils import add_custom_handler, LoggerAdapter, Colours

HOME_PATH = os.path.expanduser("~")

parser = argparse.ArgumentParser()
parser.add_argument("--one-file", type=str, required=False)
parser.add_argument("--overwrite", action=argparse.BooleanOptionalAction)

args = parser.parse_args()

ONE_FILE = args.one_file
OVERWRITE = args.overwrite

logger = add_custom_handler(logging.getLogger(Colours.CLAY.apply("💠 DotFiles")), logging.DEBUG)

def remove_file(destination):
    func_logger = LoggerAdapter(logger, prefix="remove_func")

    dest = HOME_PATH + f"/{destination}"
    func_logger.debug(f"Deleting {dest}...")

    if os.path.isdir(dest):
        if os.path.islink(dest):
            os.unlink(dest)
        else:
            shutil.rmtree(dest)
        return

    os.remove(dest)

def link_to_home(file_name: str, destination: str):
    func_logger = LoggerAdapter(logger, prefix="link_func")

    source = f"{os.path.split(__file__)[0]}/{file_name}"

    code = os.system(
        f"cd '{HOME_PATH}' && sudo ln -s '{source}' '{os.path.split(destination)[0] if os.path.isdir(source) else destination}'"
    )

    if code == 256:

        if OVERWRITE or input(Colours.ORANGE.apply(f"'{file_name}' already exists do you want to overwrite? [y/n] ")).lower() == "y":
            remove_file(destination)
            link_to_home(file_name, destination)

    else:
        func_logger.info(f"Linked {file_name} to '{destination}' successfully.")

if __name__ == "__main__":
    json_dict: dict = json.load(open("./dotfiles.json", mode="r"))
    logger.debug("Loaded dotfiles.json")

    if ONE_FILE: # Link only this one file that has been specified.
        file_name = os.path.split(os.path.abspath(ONE_FILE))[1]
        dest = json_dict.get(file_name)

        if dest is None:
            logger.error("That file is not stated in dotfiles.json! You may only install files listed in dotfiles.json")
        else:
            link_to_home(file_name, dest)

    else: # Link all files in json.
        for file_name, dest in json_dict.items():
            link_to_home(file_name, dest)