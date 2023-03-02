import random

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
        print(info)

        info = readASP('AgentPosition.gr')
        print(info)

    @staticmethod
    def decideOnNextAction():
        info = readASP('ActionRules.gr')
        agentPosition = readASP('AgentPosition.gr')["agent"][0]
        history = readASP('PreceptHistory.gr')

        if history.keys().__contains__("history"):
            agentHistory = history["history"]
            if not agentHistory.__contains__(agentPosition):
                f = open("PreceptHistory.gr", "a")
                # f is the File Handler
                f.write("\nhistory(" + str(agentPosition[0]) + "," + str(agentPosition[1]) + ").")
                f.close()
        else:
            f = open("PreceptHistory.gr", "a")
            # f is the File Handler
            f.write("\nhistory(" + str(agentPosition[0]) + "," + str(agentPosition[1]) + ").")
            f.close()

        for key,value in info.items():
            if key == "safeMove":
                for move in value:
                    print("Possible Move to " + str(move) + " (SAFE)")
            if key == "riskyMove":
                for move in value:
                    print("Possible Move to " + str(move) + " (RISKY)")

        if info.keys().__contains__("safeMove"):
            move = info["safeMove"].pop(random.randint(0,len(info["safeMove"]) - 1))
            f = open("AgentPosition.gr", "w")
            # f is the File Handler
            f.write("agent(" + str(move[0]) + "," + str(move[1]) + ").")
            f.close()
            print("Moving to " + str(move[0]) + str(move[1]))
        else:
            move = info["riskyMove"].pop(random.randint(0,len(info["riskyMove"]) - 1))
            f = open("AgentPosition.gr", "w")
            # f is the File Handler
            f.write("agent(" + str(move[0]) + "," + str(move[1]) + ").")
            f.close()


if __name__ == "__main__":

    print("Wumpus World: Game Started:")
    WumpusAgent = KBAgent
    while True:
        WumpusAgent.recieveAndSavePrecepts()
        WumpusAgent.decideOnNextAction()
