from lark import Transformer

keywords = ["bool", "break", "btoi", "class", "continue", "define", "double", "dtoi", "else", "for", "if", "import",
            "int", "itob", "itod", "new", "NewArray", "__func__", "__line__", "null", "Print", "private", "public",
            "ReadInteger", "ReadLine",
            "return", "string", "this", "void", "while"]
bools = ["true", "false"]


class MacroTransformer(Transformer):
    macro_dict = {}

    def macro(self, macro):
        macro = str(macro[0].value).split(" ", 2)
        self.macro_dict[macro[1]] = macro[2]
        pass

    def default(self, token):
        if len(token) > 0:
            if token[0].value in self.macro_dict:
                return self.macro_dict[token[0].value]
            return token[0].value
        else:
            pass

    def string(self, id):
        if id[0].value.startswith("\"") and id[0].value.endswith("\""):
            if id[0].value[1:len(id[0].value)-1] in self.macro_dict:
                return "\""+self.macro_dict[id[0].value[1:len(id[0].value)-1]]+"\""
        return self.default(id)

    operator = COMMENT = id = boolean = double = int = default


class DecafTransformer(Transformer):
    def default(self, token):
        if len(token) > 0:
            return token[0].value
        else:
            pass

    operator = default

    def COMMENT(self, token):
        pass

    def id(self, id):
        if id[0] in keywords:
            return id[0].value
        elif id[0] in bools:
            return self.boolean(id)
        else:
            return "T_ID", id[0].value

    def string(self, token):
        return "T_STRINGLITERAL", token[0].value

    DOUBLE_QUOTED_STRING = SINGLE_QUOTED_STRING = string

    def boolean(self, token):
        return "T_BOOLEANLITERAL", token[0].value

    def double(self, token):

        return "T_DOUBLELITERAL", token[0].value

    def int(self, token):
        return "T_INTLITERAL", token[0].value
