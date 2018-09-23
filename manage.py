import click
import os

from setup.populate import create_spots_from_file
from setup.clear_db import delete_all_spots


@click.group()
def cli():
    pass


@cli.command()
@click.option('--file_path', default=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                  'setup', 'spots.json'))
def populate(file_path):
    create_spots_from_file(file_path)


@cli.command()
def clear_db():
    delete_all_spots()


if __name__ == '__main__':
    cli()
