import os
import click

from directory_printer.print_directory_structure import print_directory_structure_output
from directory_printer.build_directory_structure import build_directory_structure


@click.command(help="Prints a the files and folders under current working directory.")
def print_directories():
    current_working_directory = os.getcwd()
    directory_structure = build_directory_structure(current_working_directory)
    print_directory_structure_output(directory_structure)


if __name__ == "__main__":
    print_directories()
