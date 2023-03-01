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
                if not returnDict.keys().__contains__(term.name):
                    returnDict[term.name] = []
                argList = []
                for a in term.arguments:
                    if a.type == SymbolType.String:
                        argList.append(a.string)
                    if a.type == SymbolType.Number:
                        argList.append(a.number)
                    if a.type == SymbolType.Function:
                        argList.append(a.name)
                returnDict[term.name].append(argList)

    return returnDict


class KBAgent:

    @staticmethod
    def recieveAndSavePrecepts():
        info = readASP('WumpusWorldConfiguration.gr')
        print(info)
        xPos = info['agent'][0]
        yPos = info['agent'][1]

        # startingXPos = xPos

        # if startingXPos != xPos:
        # f = open("AgentPosition.gr", "a")
        # f.write("\nagent(" + str(xPos) + "," + str(yPos) + ").")
        # f.close()

    @staticmethod
    def decideOnNextAction():
        print("Penis Again")


if __name__ == "__main__":

    WumpusAgent = KBAgent
    while True:
        WumpusAgent.recieveAndSavePrecepts()
        WumpusAgent.decideOnNextAction()
