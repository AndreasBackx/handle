import os
import shutil
import traceback

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

        self.root_node = ramlfications.parse(source)

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
        if os.path.exists(self.BUILD_DIR):
            shutil.rmtree(self.BUILD_DIR)

        os.makedirs(self.BUILD_DIR + '/static')

        environment = self.environment
        with open(self.BUILD_DIR + '/index.html', 'w') as fh:
            try:
                root_section = Section(
                    title=self.root_node.title,
                    docs=self.root_node.documentation
                )

                sections = [root_section]

                if self.root_node.resources:
                    for resource in self.root_node.resources:
                        if resource.parent is None:
                            sections.append(
                                Section(
                                    resource=resource
                                )
                            )
                output = environment.get_template('index.html').render(
                    sections=sections
                )
            except:
                output = '<pre>{traceback}</pre>'.format(
                    traceback=traceback.format_exc().replace('\\n', '<br/>')
                )
            fh.write(output)
