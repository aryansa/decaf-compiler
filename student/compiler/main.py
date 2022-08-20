from .error import syntax_error
from .lexer import scan_file, replace_macros


def run(input_file_address: str) -> bool:
    input_file = open(input_file_address)
    input_content = input_file.read()
    #base_file = replace_macros(input_content)
    # Tokens = scan_file(base_file)
    return syntax_error(input_content)
