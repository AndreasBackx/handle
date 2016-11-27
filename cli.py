import logging.config

import click
from handle.handle import Handle
from livereload import Server


@click.group()
@click.option('--verbose', is_flag=True, help='Show verbose logging messages.')
@click.option('--config', help='Add ramlfications config file.')
@click.argument('source')
@click.pass_context
def cli(context, source, config, verbose):
    if context.obj is None:
        context.obj = {}
    context.obj['source'] = source
    context.obj['config'] = config
    context.obj['verbose'] = verbose

    level = 'DEBUG' if verbose else 'INFO'
    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'colored': {
                '()': 'colorlog.ColoredFormatter',
                'format': (
                    '%(yellow)s[%(asctime)s] '
                    '%(log_color)s[%(levelname)s] '
                    '%(reset)s%(message)s'
                ),
                'datefmt': '%H:%M',
                'log_colors': {
                    'DEBUG': 'cyan',
                    'INFO': 'green',
                    'WARNING': 'purple',
                    'ERROR': 'red',
                    'CRITICAL': 'red,bold',
                },
                'style': '%'
            }
        },
        'handlers': {
            'default': {
                'level': level,
                'formatter': 'colored',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': level,
                'propagate': True
            },
        }
    })


@cli.command()
@click.pass_context
def build(context):
    handle = Handle(
        source=context.obj['source']
    )
    handle.build()


@cli.command()
@click.option('--port', default=8000, help='Specify port to use for livereload server.')
@click.option('--host', default='0.0.0.0', help='Specify host to use for livereload server.')
@click.pass_context
def serve(context, port, host):
    handle = Handle(
        source=context.obj['source'],
        config=context.obj['config']
    )
    handle.build()
    logging.info('Initial files built.')

    def on_update():
        logging.info('Change detected...')
        handle.build()
        logging.info('Project updated.')

    server = Server()
    server.watch(handle.template_dir, on_update)

    logging.info(
        'Spinning up Handle livereload server at "%s:%d"...',
        host, port
    )
    server.serve(
        root=handle.BUILD_DIR,
        port=port,
        host=host,
        debug=True
    )
    logging.info('Stopping the Handle livereload server...')
