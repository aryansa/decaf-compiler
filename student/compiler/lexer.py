from lark import Lark

from .transformers import DecafTransformer, MacroTransformer


def new_lexer():
    return None


def scan_line(line: str):
    result = pare_to_child(line)
    return result.children


def replace_macros(code: str):
    parser = get_parser(code)
    transformer = MacroTransformer()
    result = transformer.transform(parser)
    return children_to_file(result.children)


def get_parser(code: str):
    parser = Lark.open('../decaf.lark', rel_to=__file__, parser="lalr", priority="invert")
    tree = parser.parse(code)
    return tree


def pare_to_child(code: str):
    tree = get_parser(code)
    transformer = DecafTransformer()
    return transformer.transform(tree)


def children_to_file(children):
    my_string = ''
    for t in children:
        if t is not None:
            if type(t) is tuple:
                my_string += ' '.join(t)
            else:
                my_string += str(t)
            my_string += "\n"
    return my_string


def scan_file(line: str):
    zena = pare_to_child(line)
    return children_to_file(zena.children)
