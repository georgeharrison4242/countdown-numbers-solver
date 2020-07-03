import itertools
from expression import *

class Generator:
    # provides functions to generate expression-value pairs and all choices
    # from a given list. primarily to hide these functions from solver interface
    def __init__(self):
        pass

    # genChoices: [Int] -> [[Int]]
    # genChoices returns all non-empty subsequences of permutations of ns
    # e.g. genChoices([1,2]) = [[1],[2],[1,2],[2,1]]
    def genChoices(self, ns):

        # generate all subsets ns
        subsets = []
        for i in range(1,len(ns)+1):
            subsets += list(itertools.combinations(ns,i))
        
        # and all permutations of such sets
        permutations = []
        for s in subsets:
            permutations += list(itertools.permutations(s))

        # convert tuples to lists
        choices = list(map(lambda p: list(p), permutations))

        return choices


    # genExprs: [Int] -> [(Expression,Int)]
    # genExprs returns all expression-value pairs for a list of numbers ns
    def genExprs(self, ns):

        return self.exprs(ns, [Add(), Sub(), Mul(), Div()])

    def exprs(self, ns, ops):
        es = []
        if len(ns)==1: # only one tree possible for one number
            return [(Val(ns[0]),ns[0])]
        else:
            # find splits of ns, e.g. [1,2,3] -> [([1],[2,3]),([1,2],[3])]
            splits = [ (ns[:i],ns[i:]) for i in range(1,len(ns)) ]

            for split in splits:
                # compute all expressions/values for left and right subtrees of a split
                ls = self.exprs(split[0],ops)
                rs = self.exprs(split[1],ops)

                for (le,lv) in ls:
                    for (re,rv) in rs:
                        for op in ops:

                            expr =  App(op,le,re)
                            (val,valid) = op.apply(lv,rv)

                            if valid:
                                es += [(expr,val)]
        return es