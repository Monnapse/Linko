"""

    Made by Monnapse#7578

"""

from Linko import Linko, render, render_layers
from flask import Flask

app = Flask(__name__)
Link = Linko()

views=0
def page_views():
    global views
    views+=1
    return views

Link.add_method("GetPageViews", page_views)

@app.route("/")
def home():
    localLink = Link.create_layer()
    localLink.add_method("PageName", "Home Page")

    HomePage = """
    <!DOCTYPE html>

    <html>
        <title>[[! PageName !]]</title>
    <head>

    </head>

    <body>
        Page Views [[! GetPageViews !]]
    </body>

    </html>
    """

    return render_layers(HomePage, {Link, localLink})

@app.route("/sub")
def sub():
    localLink = Link.create_layer()
    localLink.add_method("PageName", "Sub Page")
    localLink.add_method("Sub", "Sub page works")

    SubPage = """
    <!DOCTYPE html>

    <html>
        <title>[[! PageName !]]</title>
    <head>

    </head>

    <body>
        Sub [[! Sub !]]
    </body>

    </html>
    """

    return localLink.render(SubPage)

if __name__ == '__main__':
    app.run(debug=True)