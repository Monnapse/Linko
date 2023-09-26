import re
import types

style = r'\[\[!(.*?)!\]\]'
#style = r'\[\[! (?:.*?|\[\[!.*?!\]\])*? !\]\]'
function = r'^\w+\(.*\)$'
    
class Linko:     
    def __init__(self, Layers: set = {}, Methods: set = {}):
       """
       Connect Python and HTML to pass varius Methods.

       [[! valueHere !]]
       """
       self.Layers = Layers
       self.Methods = Methods
        
    def add_method(self, Method: str or types.FunctionType, Value: any or callable or None = None) -> None:
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

            #if re.match(function, match):
                #function
            #else:
            try:
                value = self.Methods[stripped]

                if callable(value):
                    content = content.replace(f"[[!{match}!]]", str(value()), 1)
                elif value:
                    content = content.replace(f"[[!{match}!]]", value, 1)
            except:
                print(f"Nothing assigned to {stripped}")

        return content