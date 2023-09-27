from Linko import Linko, render_layers, render

# Global stuff
globalLink = Linko()

# Static, stuff that stay the same the entire site | top navbar, bottom navbar
globalStatic = globalLink.create_layer()

# globals
html_template = open('visuals/templates/template.html', 'r').read()
globalStatic.add_method("Static", open('visuals/templates/static.html', 'r').read())
globalLink.add_method("Loader", open('visuals/templates/loading.html', 'r').read())

# Home Page
home = globalLink.create_layer()
home.add_method("PageName", "Home Page")
home.add_method("Content", open('visuals/templates/index.html', 'r').read())

homepage = render_layers(html_template, {home, globalStatic})

# Other Page
other = globalLink.create_layer()
other.add_method("PageName", "Other Page")
other.add_method("Content", open('visuals/templates/index.html', 'r').read())

otherpage = render_layers(html_template, {other, globalStatic})