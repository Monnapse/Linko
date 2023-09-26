import re

class Linko:
    def __init__(self, Methods: set = {}):
       """
       Connect Python and HTML to pass varius Methods.

       [[! function() !]]
       [[! valueHere !]]
       [[! valueHere !]]
       """
       self.Methods = Methods

    def add_method(self, Method: str, Value: any) -> None:
        """
        adds method to the Methods set
        """
        print(Method, Value)
        self.Methods[Method] = Value

    def render(self, content: str) -> str:
        pattern = r'\[\[! (.*?) !\]\]'
        matches = re.findall(pattern, content)

        for match in matches:
            print(f"[[! {match} !]]", self.Methods[match])
            content = content.replace(f"[[! {match} !]]", self.Methods[match], 1)

        return content