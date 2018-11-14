def process(app):
    app.static('css', './templates/css')
    app.static('img', './templates/img')
    app.static('js', './templates/js')
    app.static('scss', './templates/scss')
    app.static('vendor', './templates/vendor')
    app.static('device-mockups', './templates/device-mockups')
