"""Script para agregar archivos al .driveignore"""

import click
import os


@click.command()
@click.argument("file", nargs=-1)
def main(file):
    '''Agrega ruta al archivo .driveignore'''
    with open(os.getcwd() + '/.driveignore','at') as f:
        for path in file:
            f.write(path+'\n')


if __name__ == "__main__":
    main()