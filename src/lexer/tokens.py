import enum

class Tokens(enum.Enum):
    # KEYWORDS
    PRINT = 1
    INPUT = 2
    LET = 3
    GOTO = 4
    IF = 5
    GOSUB = 6
    RETURN = 7
    THEN = 8
    CLEAR = 9
    LIST = 10
    RUN = 11
    END = 12
    # SEPERATORS
    COMMA = 13
    NL = 14
    # LITERALS
    NUMBER = 15
    STRING = 16
    # OPERATORS
    PLUS = 17
    MINUS = 18
    MULTIPLY = 19
    DIVIDE = 20
    LT = 21
    LEQ = 22
    GT = 23
    GEQ = 24
    EQ = 25
    # IDENTIFIERS
    IDENTIFIER = 26

class TokenTypes(enum.Enum):
    KEYWORDS = 1
    SEPARATORS = 2
    LITERALS = 3
    OPERATORS = 4
    IDENTIFIER = 24

def getType(token: Tokens) -> TokenTypes:
    m = {
        Tokens.PRINT: TokenTypes.KEYWORDS,
        Tokens.INPUT: TokenTypes.KEYWORDS,
        Tokens.LET: TokenTypes.KEYWORDS,
        Tokens.GOTO: TokenTypes.KEYWORDS,
        Tokens.IF: TokenTypes.KEYWORDS,
        Tokens.GOSUB: TokenTypes.KEYWORDS,
        Tokens.RETURN: TokenTypes.KEYWORDS,
        Tokens.THEN: TokenTypes.KEYWORDS,
        Tokens.CLEAR: TokenTypes.KEYWORDS,
        Tokens.LIST: TokenTypes.KEYWORDS,
        Tokens.RUN: TokenTypes.KEYWORDS,
        Tokens.END: TokenTypes.KEYWORDS,
        Tokens.COMMA: TokenTypes.SEPARATORS,
        Tokens.NL: TokenTypes.SEPARATORS,
        Tokens.NUMBER: TokenTypes.LITERALS,
        Tokens.STRING: TokenTypes.LITERALS,
        Tokens.PLUS: TokenTypes.OPERATORS,
        Tokens.MINUS: TokenTypes.OPERATORS,
        Tokens.MULTIPLY: TokenTypes.OPERATORS,
        Tokens.DIVIDE: TokenTypes.OPERATORS,
        Tokens.LT: TokenTypes.OPERATORS,
        Tokens.GEQ: TokenTypes.OPERATORS,
        Tokens.GT: TokenTypes.OPERATORS,
        Tokens.GEQ: TokenTypes.OPERATORS,
        Tokens.EQ: TokenTypes.OPERATORS,
        Tokens.IDENTIFIER: TokenTypes.IDENTIFIER
    }
    return m[token]
