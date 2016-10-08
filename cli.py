import logging

import click
from handle.handle import Handle


@click.command()
@click.option('--verbose', is_flag=True, help='Show verbose logging messages.')
@click.argument('source')
def build(source, verbose):
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format='%(message)s'
    )

    handle = Handle(source=source)
    handle.build()
