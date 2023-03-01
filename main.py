from clingo import Control
from clingo import SymbolType
import numpy as np


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

def printWorld(dict,agent):
    twoDimArr = [[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]
    for i in dict.keys():
        coords = dict[i]
        if len(coords) > 0:
            if i == "wumpus":
                toReplace = "w"
            elif i == "pit":
                toReplace = "p"
            elif i == "gold":
                toReplace = "g"

            for pair in coords:
                if isinstance(pair, int):
                    twoDimArr[coords[0]-1][coords[1]-1] = toReplace
                    break
                twoDimArr[pair[0]-1][pair[1]-1] = toReplace
    xPos = agent['agent'][0][0]
    yPos = agent['agent'][0][1]
    twoDimArr[xPos-1][yPos-1] = "A"

    print(np.fliplr(np.rot90(np.flipud(np.matrix(twoDimArr)))))

class KBAgent:

    @staticmethod
    def recieveAndSavePrecepts():
        info = readASP('PreceptRules.gr')
        previousInfo = readASP('PreceptHistory.gr')

        print(previousInfo)



if __name__ == "__main__":

    WumpusAgent = KBAgent
    while True:
        WumpusAgent.recieveAndSavePrecepts()
        # WumpusAgent.decideOnNextAction()
