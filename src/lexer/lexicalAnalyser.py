import re
from typing import Generator, Tuple
from .tokens import Tokens


class LexicalAnalyser:
    def analyse(self, code: str) -> Generator[Tuple[Tokens, str | int], None, None]:
        ptr = 0
        while ptr < len(code):
            ch = code[ptr]
            # LITERALS
            if ch == "\"":
                # encountered a string
                ptr += 1
                str_buff = ""
                while ptr < len(code) and (_ch := code[ptr]) != "\"":
                    if re.match(r"[\w\s!?']", _ch):
                        str_buff += _ch
                        ptr += 1
                    # Two error states if we can't terminate the string
                    else:
                        print(str_buff, ptr, _ch)
                        raise SyntaxError()
                if ptr == len(code):
                    raise SyntaxError()
                yield (Tokens.STRING, str_buff)
            elif ch.isdigit():
                # parse the number
                int_buff = int(ch)
                while ptr + 1 < len(code) and (_ch := code[ptr + 1]) not in [" ", "\n"]:
                    if _ch.isdigit():
                        int_buff = 10 * int_buff + int(_ch)
                        ptr += 1
                    else:
                        raise SyntaxError()
                yield (Tokens.NUMBER, int_buff)
            # SEPARATORS
            elif ch == "\n":
                # New line
                yield (Tokens.NL, ch)
            elif ch == " ":
                # Space, continue
                pass
            elif ch == ",":
                yield (Tokens.COMMA, ch)
            # OPERATORS
            elif ch == "+":
                yield (Tokens.PLUS, ch)
            elif ch == "-":
                yield (Tokens.MINUS, ch)
            elif ch == "*":
                yield (Tokens.MULTIPLY, ch)
            elif ch == "/":
                yield (Tokens.DIVIDE, ch)
            elif ch == "<":
                if ptr + 1 < len(code) and code[ptr + 1] == "=":
                    ptr += 1
                    yield (Tokens.LEQ, ch + code[ptr])
                else:
                    yield (Tokens.LT, ch)
            elif ch == ">":
                if ptr + 1 < len(code) and code[ptr + 1] == "=":
                    ptr += 1
                    yield (Tokens.GEQ, ch + code[ptr])
                else:
                    yield (Tokens.GT, ch)
            elif ch == "=":
                yield (Tokens.EQ, ch)
            # IDENTIFIER/KEYWORD
            elif ch.isupper():
                cmd_buff = ch
                while ptr + 1< len(code) and (_ch := code[ptr + 1]) not in [" ", "\n", ","]:
                    if _ch.isupper():
                        cmd_buff += _ch
                        ptr += 1
                    else:
                        raise SyntaxError()
                # Check for keyword matches
                if cmd_buff == "PRINT":
                    yield (Tokens.PRINT, cmd_buff)
                elif cmd_buff == "INPUT":
                    yield (Tokens.INPUT, cmd_buff)
                elif cmd_buff == "LET":
                    yield (Tokens.LET, cmd_buff)
                elif cmd_buff == "GOTO":
                    yield (Tokens.GOTO, cmd_buff)
                elif cmd_buff == "IF":
                    yield (Tokens.IF, cmd_buff)
                elif cmd_buff == "GOSUB":
                    yield (Tokens.GOSUB, cmd_buff)
                elif cmd_buff == "RETURN":
                    yield (Tokens.RETURN, cmd_buff)
                elif cmd_buff == "THEN":
                    yield (Tokens.THEN, cmd_buff)
                elif cmd_buff == "CLEAR":
                    yield (Tokens.CLEAR, cmd_buff)
                elif cmd_buff == "LIST":
                    yield (Tokens.LIST, cmd_buff)
                elif cmd_buff == "RUN":
                    yield (Tokens.RUN, cmd_buff)
                elif cmd_buff == "END":
                    yield (Tokens.END, cmd_buff)
                # Otherwise we have a variable
                else:
                    yield (Tokens.IDENTIFIER, cmd_buff)
            else:
                raise SyntaxError()
            ptr += 1
            