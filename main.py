from clingo import Control
from clingo import SymbolType


class KBAgent:

    @staticmethod
    def recieveAndSavePrecepts():
        print("Penis")

    @staticmethod
    def decideOnNextAction():
        print("Penis Again")


if __name__ == "__main__":

    ctl = Control(["0"])
    ctl.load('prgm1.lp')
    ctl.ground([("base", [])])
    cnt=0
    with ctl.solve(yield_=True) as hnd:
        for m in hnd:
            print('Model' + str(cnt))
            for term in m.symbols(shown=True):
                argList=[]
                for a in term.arguments:
                    if a.type == SymbolType.String:
                        argList.append(a.string)
                    if a.type == SymbolType.Number:
                        argList.append(a.number)
                    if a.type == SymbolType.Function:
                        argList.append(a.name)
                print(term.name, argList)

    WumpusAgent = KBAgent

    # while True:

        # WumpusAgent.recieveAndSavePrecepts()
        # WumpusAgent.decideOnNextAction()

