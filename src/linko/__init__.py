import re
import types

style = r'\[\[!(.*?)!\]\]'
#style = r'\[\[! (?:.*?|\[\[!.*?!\]\])*? !\]\]'
function = r'^\w+\(.*\)$'
    
class Linko:     
    def __init__(self, Methods: set = {}):
       """
       Connect Python and HTML to pass varius Methods.

       [[! function() !]]
       [[! valueHere !]]
       [[! valueHere !]]
       """
       self.Methods = Methods
        
    def add_method(self, Method: str or types.FunctionType, Value: any or None = None) -> None:
        """
        adds method to the Methods set
        """
        if callable(Method):
            self.Methods[Method.__name__] = Method
        else:
            self.Methods[Method] = Value

    def render(self, content: str) -> str:
        matches = re.findall(style, content)
        
        for match in matches:
            stripped = match.strip()

            if re.match(function, match):
                print(f"'{match}' resembles a function call.")
            else:
                print(f"'{match}' does not resemble a function call.")
                value = self.Methods[stripped]
                if value:
                    content = content.replace(f"[[!{match}!]]", value, 1)

        return content