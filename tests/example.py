"""

    Made by Monnapse#7578

"""

from Linko import Linko
from flask import Flask

app = Flask(__name__)
globalLink = Linko()

views=0
def page_views():
    global views
    views+=1
    return views

globalLink.add_method("GetPageViews", page_views)

@app.route("/")
def home():
    localLink = Linko()
    print(localLink.Methods)
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

    return localLink.render(HomePage)

if __name__ == '__main__':
    app.run(debug=True)