from setuptools import setup
from handle import __version__

setup(
    name='handle',
    version=__version__,
    description='A RAML to HTML parser.',
    author='Andreas Backx',
    author_email='andreas@backx.org',
    url='https://github.com/AndreasBackx/handle',
    download_url='https://github.com/AndreasBackx/handle/tarball/' + __version__,
    keywords=[
        'raml',
        'html'
    ],
    packages=[
        'handle'
    ],
    dependency_links=[
        'http://github.com/spotify/ramlfications.git@v0.2.0-dev#egg=ramlfications'
    ],
    install_requires=[
        'click==6.6',
        'colorlog==2.7.0',
        'jac==0.15.3',
        'jinja2==2.8',
        'livereload==2.4.1',
        'pygments==2.1.3',
        'ramlfications==0.2.0'
    ],
    entry_points={
        'console_scripts': [
            'handle = cli:cli'
        ]
    }
)
