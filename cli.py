import click
from handle.handle import Handle


@click.command()
@click.argument('source')
def build(source):
    handle = Handle(source=source)
    handle.build()
