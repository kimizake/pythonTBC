import enum
from ..lexer import Tokens

class Grammar(enum.Enum):
    PROGRAM = 0
    LINELIST = 1
    LINE = 2
    STATEMENT = 3
    EXPRLIST = 4
    VARLIST = 5
    EXPR = 6
    BASEXPR = 7
    TERM = 8
    FACTOR = 9
    RELOP = 10

BNF = {
    Grammar.PROGRAM: [
        [Grammar.LINELIST]
    ],
    Grammar.LINELIST: [
        [Grammar.LINE, Tokens.NL, Grammar.LINELIST],
        [Grammar.LINE, Tokens.NL],
        [Grammar.LINE],
    ],
    Grammar.LINE: [
        [Tokens.NUMBER, Grammar.STATEMENT],
        [Grammar.STATEMENT],
    ],
    Grammar.STATEMENT: [
        [Tokens.IF, Grammar.EXPR, Grammar.RELOP, Grammar.EXPR, Tokens.THEN, Grammar.STATEMENT],
        [Tokens.PRINT, Grammar.EXPRLIST],
        [Tokens.GOTO, Grammar.EXPR],
        [Tokens.INPUT, Grammar.VARLIST],
        [Tokens.LET, Tokens.IDENTIFIER, Tokens.EQ, Grammar.EXPR],
        [Tokens.GOSUB, Grammar.EXPR],
        [Tokens.RETURN],
        [Tokens.CLEAR],
        [Tokens.LIST],
        [Tokens.RUN],
        [Tokens.END],
    ],
    Grammar.EXPRLIST: [
        [Tokens.STRING, Tokens.COMMA, Grammar.EXPRLIST],
        [Grammar.EXPR, Tokens.COMMA, Grammar.EXPRLIST],
        [Tokens.STRING],
        [Grammar.EXPR],
    ],
    Grammar.VARLIST: [
        [Tokens.IDENTIFIER, Tokens.COMMA, Grammar.VARLIST],
        [Tokens.IDENTIFIER],
    ],
    Grammar.BASEXPR: [
        [Grammar.TERM, Tokens.PLUS, Grammar.BASEXPR],
        [Grammar.TERM, Tokens.MINUS, Grammar.BASEXPR],
        [Grammar.TERM],
    ],
    Grammar.EXPR: [
        [Tokens.STRING],
        [Tokens.PLUS, Grammar.TERM, Grammar.BASEXPR],
        [Tokens.MINUS, Grammar.TERM, Grammar.BASEXPR],
        [Grammar.BASEXPR],
        [Tokens.PLUS, Grammar.TERM],
        [Tokens.MINUS, Grammar.TERM],
    ],
    Grammar.TERM: [
        [Grammar.FACTOR, Tokens.MULTIPLY, Grammar.TERM],
        [Grammar.FACTOR, Tokens.DIVIDE, Grammar.TERM],
        [Grammar.FACTOR],
    ],
    Grammar.FACTOR: [
        [Tokens.IDENTIFIER],
        [Tokens.NUMBER],
        [Grammar.EXPR]
    ],
    Grammar.RELOP: [
        [Tokens.EQ],
        [Tokens.LT],
        [Tokens.LEQ],
        [Tokens.GT],
        [Tokens.GEQ],
    ]
}
