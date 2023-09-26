from Linko import Linko

Link = Linko()
Link.add_method("Test", "Variables work Yes")

def call_test(argument, test):
    return argument + " | " + test

Link.add_method(, "Variables work Yes")

HTML = """
<!DOCTYPE html>

<html>
    [[! Test !]]
<head>

</head>

<body background="drive/media/png/backdrop.png">

</body>

</html>
"""

print(Link.render(HTML))