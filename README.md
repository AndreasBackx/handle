A RAML documentation generator that generates HTML from RAML documentation files. The 0.2.0 development version of ramlfications is currently used for parsing. Handle currently is very explicit because no information about inheritance is given by ramlfications.

# Installation

	pip install -e git+git://github.com/spotify/ramlfications.git@v0.2.0-dev#egg=ramlfications
	pip install handle

# How to use

Start a simple livereload server that automatically updates and refreshes the browser when a change to handle or a template is detected:

	handle api.raml serve

Build the HTML documentation once:

	handle api.raml build

Pass an extra ramlfications config file:

	handle --config config.ini api.raml serve

Pass `--verbose` for more verbose logging. More help:

	handle --help
