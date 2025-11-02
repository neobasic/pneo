from enum import StrEnum, auto
from typing import Optional

from antlr4 import InputStream, FileStream, CommonTokenStream, ParserRuleContext

from ngne.frontend.ast_tree_listener import AstTreeListener
from ngne.frontend.neobasic_extended_lexer import NeoBasicExtendedLexer
from ngne.frontend.neobasic_extended_parser import NeoBasicExtendedParser
from nuke import gettext as _
from nuke.formatters.print_color import p_error


class EProgram(StrEnum):
    ONE_LINER = auto()
    SCRIPT = auto()
    SOURCE_CODE = auto()


def _parse_neobasic_stream(input_stream: InputStream, prog_opt: EProgram = EProgram.ONE_LINER) -> Optional[
    AstTreeListener]:
    # initialize parsing components
    lexer = NeoBasicExtendedLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = NeoBasicExtendedParser(stream)

    # construct an Antlr AST from the given NeoBASIC code
    tree: Optional[ParserRuleContext] = None
    match prog_opt:
        case EProgram.ONE_LINER:
            tree = parser.oneLinerProgram()
        case EProgram.SCRIPT:
            tree = parser.scriptProgram()
        case EProgram.SOURCE_CODE:
            tree = parser.sourceCodeProgram()
        case _:
            tree = None

    if tree: print(tree.toStringTree(recog=parser))

    # from the Antlr AST, generate the complete NeoBASIC language AST
    listener = AstTreeListener()
    # walker = ParseTreeWalker()
    # walker.walk(listener, tree)

    return listener


def parse_one_liner(liner: str) -> Optional[AstTreeListener]:
    if not liner: return None

    # code: str = liner if liner.endswith("\n") else liner + "\n"
    input_stream: InputStream = InputStream(liner)
    return _parse_neobasic_stream(input_stream, EProgram.ONE_LINER)


def parse_source_code(code: str) -> Optional[AstTreeListener]:
    if not code: return None

    input_stream: InputStream = InputStream(code)
    return _parse_neobasic_stream(input_stream, EProgram.SOURCE_CODE)


def parse_source_file(filename: str) -> Optional[AstTreeListener]:
    """
    Parse the entire content of a text source file.

    Args:
        filename (str): The path to the file to be read.

    Returns:
        Optional[AstTreeListener]: The resulting NeoBASIC AST if successful; otherwise None.

    Handles:
        - FileNotFoundError: File does not exist.
        - PermissionError: Insufficient permission to read file.
        - IsADirectoryError: Path points to a directory, not a file.
        - UnicodeDecodeError: File cannot be decoded using UTF-8.
        - OSError: Generic I/O or system-related error.
        - Exception: Any other unforeseen error.
    """

    if not filename: return None

    # first, try to open and read the file.
    try:
        # Read the first line just to check (and raise errors if any)
        with open(filename, 'r', encoding='utf-8') as sf:
            sf.readline()

        # Now can read and parse the file from the start again
        input_stream: FileStream = FileStream(filename, encoding='utf-8')
        return _parse_neobasic_stream(input_stream, EProgram.SCRIPT)

    except FileNotFoundError:
        p_error(_("Error: File not found -> %s"), filename)
    except PermissionError:
        p_error(_("Error: Permission denied -> %s"), filename)
    except IsADirectoryError:
        p_error(_("Error: The path is a directory, not a file -> %s"), filename)
    except UnicodeDecodeError:
        p_error(_("Error: Cannot decode file with UTF-8 -> %s"), filename)
    except OSError as e:
        p_error(_("OS error while reading '%s': %r"), filename, e)
    except Exception as e:
        p_error(_("Unexpected error while reading '%s': %s -> %r"), filename, type(e).__name__, e)

    return None
