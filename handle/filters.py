import json

import xmltodict
from pygments import highlight as pygments_highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_for_mimetype


def highlight(code, mime_type):
    # ramlfications for some reason parses example data and doesn't keep the raw value of the example
    # Except in the Body.raw, but that contains everything.
    if not isinstance(code, str):
        if mime_type == 'application/json':
            code = json.dumps(code, indent=4)
        elif mime_type in ['application/rss+xml', 'application/xml']:
            code = xmltodict.unparse(code, indent=4)
    return pygments_highlight(
        code,
        get_lexer_for_mimetype(mime_type),
        HtmlFormatter(lineos=False)
    )
