from clingo import Control
from clingo import SymbolType

def readASP(filename):
    ctl = Control(["0"])
    ctl.load(filename)
    ctl.ground([("base", [])])
    returnDict = {}
    with ctl.solve(yield_=True) as hnd:
        for m in hnd:
            for term in m.symbols(shown=True):
                argList = []
                for a in term.arguments:
                    if a.type == SymbolType.String:
                        argList.append(a.string)
                    if a.type == SymbolType.Number:
                        argList.append(a.number)
                    if a.type == SymbolType.Function:
                        argList.append(a.name)
                returnDict[term.name] = argList

    return returnDict

class KBAgent:

    @staticmethod
    def recieveAndSavePrecepts():

        info = readASP('AgentPosition.gr')
        print(info)
        xPos = info['agent'][0]
        yPos = info['agent'][1]


    @staticmethod
    def decideOnNextAction():
        print("Penis Again")


if __name__ == "__main__":

    WumpusAgent = KBAgent
    while True:

        WumpusAgent.recieveAndSavePrecepts()
        WumpusAgent.decideOnNextAction()

