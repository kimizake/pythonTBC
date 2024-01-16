import re
from typing import List, Tuple
from .tokens import Tokens


class LexicalAnalyser:
    def analyse(self, code: str) -> List[Tuple[Tokens, str | int]]:
        ans = []
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
                ans.append((Tokens.STRING, str_buff))
            elif ch.isdigit():
                # parse the number
                int_buff = int(ch)
                while ptr + 1 < len(code) and (_ch := code[ptr + 1]) not in [" ", "\n"]:
                    if _ch.isdigit():
                        int_buff = 10 * int_buff + int(_ch)
                        ptr += 1
                    else:
                        raise SyntaxError()
                ans.append((Tokens.NUMBER, int_buff))
            # SEPARATORS
            elif ch == "\n":
                # New line
                ans.append((Tokens.NL, ch));
            elif ch == " ":
                # Space, continue
                pass
            elif ch == ",":
                ans.append((Tokens.COMMA, ch))
            # OPERATORS
            elif ch == "+":
                ans.append((Tokens.PLUS, ch))
            elif ch == "-":
                ans.append((Tokens.MINUS, ch))
            elif ch == "*":
                ans.append((Tokens.MULTIPLY, ch))
            elif ch == "/":
                ans.append((Tokens.DIVIDE, ch))
            elif ch == "<":
                if ptr + 1 < len(code) and code[ptr + 1] == "=":
                    ptr += 1
                    ans.append((Tokens.LEQ, ch + code[ptr]))
                else:
                    ans.append((Tokens.LT, ch))
            elif ch == ">":
                if ptr + 1 < len(code) and code[ptr + 1] == "=":
                    ptr += 1
                    ans.append((Tokens.GEQ, ch + code[ptr]))
                else:
                    ans.append((Tokens.GT, ch))
            elif ch == "=":
                ans.append((Tokens.EQ, ch))
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
                    ans.append((Tokens.PRINT, cmd_buff))
                elif cmd_buff == "INPUT":
                    ans.append((Tokens.INPUT, cmd_buff))
                elif cmd_buff == "LET":
                    ans.append((Tokens.LET, cmd_buff))
                elif cmd_buff == "GOTO":
                    ans.append((Tokens.GOTO, cmd_buff))
                elif cmd_buff == "IF":
                    ans.append((Tokens.IF, cmd_buff))
                elif cmd_buff == "GOSUB":
                    ans.append((Tokens.GOSUB, cmd_buff))
                elif cmd_buff == "RETURN":
                    ans.append((Tokens.RETURN, cmd_buff))
                elif cmd_buff == "THEN":
                    ans.append((Tokens.THEN, cmd_buff))
                elif cmd_buff == "CLEAR":
                    ans.append((Tokens.CLEAR, cmd_buff))
                elif cmd_buff == "LIST":
                    ans.append((Tokens.LIST, cmd_buff))
                elif cmd_buff == "RUN":
                    ans.append((Tokens.RUN, cmd_buff))
                elif cmd_buff == "END":
                    ans.append((Tokens.END, cmd_buff))
                # Otherwise we have a variable
                else:
                    ans.append((Tokens.IDENTIFIER, cmd_buff))
            else:
                raise SyntaxError()
            ptr += 1
        return ans
            