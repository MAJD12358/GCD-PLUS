from antlr4 import *
from GCDplusLexer import GCDplusLexer
from GCDplusParser import GCDplusParser

# Extend the parser and override the default error handler
class MyErrorListener(ParseTreeListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax Error at line {line}:{column} - {msg}")

def main():
    # Read input GCD+ code from a file
    with open('input.gcd+', 'r') as file:
        gcdPlusCode = file.read()

    # Create an ANTLR input stream from the GCD+ code
    stream = InputStream(gcdPlusCode)

    # Create a lexer that reads from the input stream
    lexer = GCDplusLexer(stream)

    # Create a buffer of tokens pulled from the lexer
    tokenStream = CommonTokenStream(lexer)

    # Create a parser that reads from the token stream
    parser = GCDplusParser(tokenStream)

    # Attach custom error listener
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())

    # Start parsing from the program rule
    tree = parser.program()

    # Print the parse tree
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
  
