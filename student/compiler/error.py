import lark
from lark import Lark


def syntax_error(code: str) -> bool:

    parser = Lark.open('./grammars/syntax.lark', rel_to=__file__, parser="lalr")
    try:
        parser.parse(code)
    except lark.exceptions.UnexpectedToken as e:

        return False

    return True
