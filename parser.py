from expression import *

class Lexer:

    def __init__(self):

        self.numbers = [i for i in range(10)]
        self.chars = ["(",")","+","-","x","*","/","="]

        self.legalCharacters =  self.numbers + self.chars
        

    def cleanInput(self, s):
        foldMultiply = s.replace("x","*")
        spacesRemoved = foldMultiply.replace(" ","")
        return spacesRemoved

    def lex(self, s):

        consumed = []
        unconsumed = self.cleanInput(s)
        while unconsumed!="":
            currentChar = unconsumed[0]
            if currentChar in self.chars:
                consumed.append(currentChar)
                unconsumed = unconsumed[1:]

            else: # number
                # find number end
                i = 0
                while i<len(unconsumed) and unconsumed[i].isnumeric(): i += 1
                consumed.append(unconsumed[:i])
                unconsumed = unconsumed[i:]

        return consumed 

class Parser:

    def __init__(self):
        self.lexer = Lexer()

    def parse(self, s):

        tokenised = self.lexer.lex(s)

        try:
            while len(tokenised)>0:
                nextToken, tokenised = tokenised[0], tokenised[1:]
                print(nextToken, tokenised)

        except:
            raise ValueError("Invalid expression")


l = Parser()
l.parse("5 x 7 = 35")