import os

import ramlfications
from jinja2 import Environment, FileSystemLoader

from .section import Section

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Handle:

    def __init__(self, source, template='default'):
        self.source = source
        self.template = template
        self.template_dir = os.path.join(
            BASE_DIR,
            'templates',
            template
        )

        self.root_node = ramlfications.parse(source)

    def build(self):
        print('self.root_node', self.root_node)
        print('dir(self.root_node)', dir(self.root_node))
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

        jinja_dir = os.path.join(
            self.template_dir,
            'jinja2',
        )
        print('jinja_dir', jinja_dir)
        environment = Environment(
            loader=FileSystemLoader(jinja_dir),
            trim_blocks=True
        )
        output = environment.get_template('index.html').render(
            sections=sections
        )
        build_dir = '_build'
        if not os.path.exists(build_dir):
            os.makedirs(build_dir)

        with open(build_dir + '/index.html', 'w') as fh:
            fh.write(output)
