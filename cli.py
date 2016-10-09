import logging.config
import time

import click
from handle.handle import Handle
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class HandleEventHandler(FileSystemEventHandler):

    def __init__(self, handle, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handle = handle

    def on_any_event(self, event):
        super().on_any_event(event)
        logging.info('Change detected: "%s"...', event.src_path)
        self.handle.build()
        logging.info('Project updated.')


@click.group()
@click.option('--verbose', is_flag=True, help='Show verbose logging messages.')
@click.argument('source')
@click.pass_context
def cli(context, source, verbose):
    if context.obj is None:
        context.obj = {}
    context.obj['source'] = source
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
@click.pass_context
def serve(context):
    logging.info('Spinning up Handle server...')
    handle = Handle(
        source=context.obj['source']
    )
    handle.build()

    event_handler = HandleEventHandler(
        handle=handle
    )
    observer = Observer()
    observer.schedule(
        event_handler,
        handle.template_dir,
        recursive=True
    )
    observer.start()
    logging.info('Initial files built and server running.')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
