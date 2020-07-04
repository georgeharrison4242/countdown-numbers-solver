class Expression:
    # eval: Void -> (Int,)
    # evaluates expression to value v
    # returns () if expression is invalid, and (v,) otherwise
    def eval():
        pass

    # __str__: Void -> String
    # paranthesised string form of expression
    def __str__():
        pass

class Val(Expression):
    def __init__(self, value):
        self.value = value

    def eval(self):
        if self.value>0:
            return (self.value,)
        return ()

    def __str__(self):
        return str(self.value)

class App(Expression):
    def __init__(self, op, l, r):
        self.op, self.l, self.r = op, l, r

    def eval(self):
        le, re = self.l.eval(), self.r.eval()
        if len(le+re)==2: # if l and r both valid
            (v,valid) = self.op.apply(le[0],re[0])
            if valid: return (v,)
        return ()

    def __str__(self):
        return "(" + str(self.l) + str(self.op) + str(self.r) + ")"


class Op:
    # apply: Int, Int -> (Int,Bool)
    # returns (v,valid) where valid is true if operation follows countdown rules
    def apply(l, r): pass
    def __str__(): pass

class Add(Op):
    def apply(self, l, r): return (l+r,l<=r)
    def __str__(self): return "+"

class Sub(Op):
    def apply(self, l, r): return (l-r,l>r)
    def __str__(self): return "-"

class Mul(Op):
    def apply(self, l, r): return (l*r,l!=1 and r!=1 and l<=r and l!=0 and r!=0)
    def __str__(self): return "x"

class Div(Op):
    def apply(self, l, r): return (int(l/r),l%r==0 and r!=1 and r!=0)
    def __str__(self): return "/"

