A RAML documentation generator that generates HTML from RAML documentation files. The 0.2.0 development version of ramlfications is currently used for parsing. Handle currently is very explicit because no information about inheritance is given by ramlfications.

# Installation

	pip install handle --process-dependency-links

Dependency links are currently deprecated but [won't be removed until a replacement is available](https://github.com/pypa/pip/issues/2621). Until then, this is the easiest way to install handle.

# How to use

Start a simple livereload server that automatically updates and refreshes the browser when a change to handle or a template is detected:

	handle api.raml serve

Build the HTML documentation once:

	handle api.raml build

Pass an extra ramlfications config file:

	handle --config config.ini api.raml serve

Pass `--verbose` for more verbose logging. More help:

	handle --help
