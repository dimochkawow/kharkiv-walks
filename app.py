from sanic import Sanic
from jinja2 import Environment, PackageLoader
from sanic.response import html
import statichandler
import os

app = Sanic()
templates = Environment(loader=PackageLoader('app', 'templates'))

@app.route('/')
async def home_page(request):
    template = templates.get_template('index.html')
    html_content = template.render()
    return html(html_content)

if __name__ == "__main__":
    statichandler.process(app)
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 8000)),
        workers=int(os.environ.get('WEB_CONCURRENCY', 1)),
        debug=bool(os.environ.get('DEBUG', '')))