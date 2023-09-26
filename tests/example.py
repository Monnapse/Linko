from Linko import Linko

Link = Linko()
Link.add_method("Test", "Variables work Yes")

def call_test(argument, test):
    return argument + " | " + test

Link.add_method(call_test)

HTML = """
<!DOCTYPE html>

<html>
    [[! Test !]]
<head>

</head>

<body>
    [[! call_test(Test, "Good") !]]
</body>

</html>
"""

print(Link.render(HTML))