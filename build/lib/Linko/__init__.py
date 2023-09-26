import re
import types

debug = False

style = r'\[\[!(.*?)!\]\]'
#style = r'\[\[! (?:.*?|\[\[!.*?!\]\])*? !\]\]'
function = r'^\w+\(.*\)$'
    
class Linko:
    def __init__(self, Methods: set = {}):
       """
       Connect Python and HTML to pass varius Methods.

       [[! valueHere !]]
       """
       self.Methods = Methods
        
    @classmethod
    def create_layer(cls, Methods: set = {}):
        return cls(Methods)

    def add_method(self, Method: str or types.FunctionType, Value: any or callable or None = None) -> None:
        """
        adds method to the Methods set
        """
        if callable(Method):
            self.Methods[Method.__name__] = Method
        else:
            self.Methods[Method] = Value

    def render(self, content: str):
        return render(self, content)

def render(layer, content: str) -> str:
    matches = re.findall(style, content)
    
    for match in matches:
        stripped = match.strip()

        #if re.match(function, match):
            #function
        #else:
        try:
            value = layer.Methods[stripped]
            if callable(value):
                content = content.replace(f"[[!{match}!]]", str(value()), 1)
            elif value:
                content = content.replace(f"[[!{match}!]]", value, 1)
        except:
            if debug:
                print(f"Nothing assigned to {stripped}")

    return content
    
def render_layers(content: str, layers: set = {}) -> str:
    new_content = content

    if layers != None and len(layers) > 0:
        for layer in layers:
            new_content = render(layer, new_content)

    return new_content