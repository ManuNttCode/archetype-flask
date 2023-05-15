import os
import logging

from . import create_app

app = create_app()

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

is_debug_env = True if os.environ.get('FLASK_DEBUG') == '1' else False
app.run(debug=is_debug_env, port=6060)
