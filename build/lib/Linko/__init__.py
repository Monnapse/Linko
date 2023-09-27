import re
import types

debug = False

style = r'\[\[!(.*?)!\]\]'
#style = r'\[\[! (?:.*?|\[\[!.*?!\]\])*? !\]\]'
function = r'^\w+\(.*\)$'

globalMethods = {}

class Linko:
    def __init__(self, isGlobal: bool = True):
        
       """
       Connect Python and HTML to pass varius Methods.

       [[! valueHere !]]
       """

       self.isGlobal = isGlobal
       self.Methods = {}

       #if isGlobal:
       #    global globalMethods
       #    globalMethods = {**globalMethods, **Methods}
       #else:
       #self.Methods = Methods
        
    @classmethod
    def create_layer(cls, isGlobal: bool = False):
        return cls(isGlobal)

    def add_method(self, Method: str or types.FunctionType, Value: any or callable or None = None, isGlobal: bool = False) -> None:
        """
        adds method to the Methods set
        """
        if isGlobal or self.isGlobal:
            global globalMethods
            if callable(Method):
                globalMethods[Method.__name__] = Method
            else:
                globalMethods[Method] = Value

        if callable(Method):
            self.Methods[Method.__name__] = Method
        else:
            self.Methods[Method] = Value

    def render(self, content: str, includeGlobal: bool = True):
        return render(self, content, includeGlobal)

def render(layer, content: str, includeGlobal: bool = True) -> str:
    Methods = layer.Methods

    if includeGlobal:
        Methods = {**globalMethods, **Methods}
        
    matches = re.findall(style, content)
    
    for match in matches:
        stripped = match.strip()

        #if re.match(function, match):
            #function
        #else:
        try:
            value = Methods[stripped]
            if callable(value):
                content = content.replace(f"[[!{match}!]]", str(value()), 1)
            elif value:
                content = content.replace(f"[[!{match}!]]", value, 1)
        except:
            if debug:
                print(f"Nothing assigned to {stripped}")

    return content
    
def render_layers(content: str, layers: set = {}, includeGlobal: bool = True) -> str:
    new_content = content

    if layers != None and len(layers) > 0:
        for layer in layers:
            new_content = render(layer, new_content, includeGlobal)

    return new_content