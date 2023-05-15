import os
import logging

from . import create_app

app = create_app()
app.logger.setLevel(logging.INFO)

is_debug_env = True if os.environ.get('FLASK_DEBUG') == '1' else False
app.run(debug=is_debug_env, port=6060)
