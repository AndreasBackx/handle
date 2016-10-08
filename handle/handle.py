import logging
import os
import shutil

import ramlfications
from jac import CompressorExtension
from jinja2 import Environment, FileSystemLoader

from .section import Section

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Handle:

    BUILD_DIR = os.path.join(
        os.path.abspath('.'),
        '_build'
    )
    STATIC_DIR = 'static'

    def __init__(self, source, template='default'):
        self.source = source
        self.template = template
        self.template_dir = os.path.join(
            BASE_DIR,
            'templates',
            template
        )

        logging.info('Using the "%s" template...', template)
        logging.info('Parsing RAML-file...')
        self.root_node = ramlfications.parse(source)
        logging.info('RAML-file succesfully parsed!')

    @property
    def environment(self):
        jinja_dir = os.path.join(
            self.template_dir,
            'jinja2',
        )
        env = Environment(
            loader=FileSystemLoader(jinja_dir),
            trim_blocks=True,
            extensions=[CompressorExtension]
        )
        env.compressor_output_dir = os.path.join(
            self.BUILD_DIR,
            self.STATIC_DIR
        )
        env.compressor_static_prefix = self.STATIC_DIR
        env.compressor_source_dirs = os.path.join(
            self.template_dir,
            'static',
            'scss'
        )

        return env

    def build(self):
        root_section = Section(
            title=self.root_node.title,
            docs=self.root_node.documentation
        )

        sections = [root_section]

        if self.root_node.resource_types:
            for resource_type in self.root_node.resource_types:
                sections.append(
                    Section(
                        resource_type=resource_type
                    )
                )

        build_dir = '_build'

        if os.path.exists(build_dir):
            shutil.rmtree(build_dir)
            logging.info('Removed "%s" build directory.', build_dir)

        os.makedirs(build_dir + '/static')
        logging.info('Created build directories.')

        environment = self.environment
        output = environment.get_template('index.html').render(
            sections=sections
        )

        with open(build_dir + '/index.html', 'w') as fh:
            fh.write(output)

        logging.info('Handled!')
