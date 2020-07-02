class Expression:
    # eval: Void -> Int
    def eval():
        pass

    # isValid: Void -> Bool
    def isValid():
        pass

class Val(Expression):
    def __init__(self, value):
        self.value = value

    def eval(self):
        if not self.isValid():
            raise Exception("Cannot evaluate invalid expression")
        return self.value

    def isValid(self):
        if self.value > 0:
            return True
        else:
            return False

class App(Expression):
    def __init__(self, op, l, r):
        self.op, self.l, self.r = op, l, r

    def eval(self):
        if not self.isValid():
            raise Exception("Cannot evaluate invalid expression") 
        return self.op.apply(self.l.eval(), self.r.eval())

    def isValid(self):
        return (self.l.isValid() and
               self.r.isValid() and
               self.op.validOp(self.l.eval(),self.r.eval()))




class Op:
    # apply: Int, Int -> Int
    def apply(l, r): pass

    # validOp: Int, Int -> Bool
    def validOp(l, r): pass

class Add(Op):
    def apply(self, l, r): return l + r
    def validOp(self, l, r): return True

class Sub(Op):
    def apply(self, l, r): return l - r
    def validOp(self, l, r): return l > r

class Mul(Op):
    def apply(self, l, r): return l * r
    def validOp(self, l, r): return True

class Div(Op):
    def apply(self, l, r): return int(l / r)
    def validOp(self, l, r): return l % r == 0

