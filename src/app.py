import os

from . import create_app

app = create_app()

is_debug_env = True if os.environ.get('FLASK_DEBUG') == '1' else False
app.run(debug=is_debug_env, port=6060)
