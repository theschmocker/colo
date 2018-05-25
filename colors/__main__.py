import click

from .colors_cli import convert_to_all

@click.command()
@click.argument('color')
def cli(color):
    click.echo(convert_to_all(color))
