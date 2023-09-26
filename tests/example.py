from Linko import Linko
import time

Link = Linko()
Link.add_method("Test", "Variables work Yes")

e=0
def call_test():
    global e
    e+=1
    return e

Link.add_method("call_test", call_test)

#def call_test(argument, test):
#    return argument + " | " + test
#
#Link.add_method(call_test)

HTML = """
<!DOCTYPE html>

<html>
    [[! Test !]]
<head>

</head>

<body>
    [[! call_test !]]
    [[! call_test !]]
    [[! call_test !]]
</body>

</html>
"""

print(Link.render(HTML))