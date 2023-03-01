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
    twoDimArr[xPos][yPos] = "A"

    print(np.flipud(np.matrix(twoDimArr)))


def generatePrecepts(agentInfo, worldInfo):

    xPos = agentInfo['agent'][0][0]
    yPos = agentInfo['agent'][0][1]

    playerLocation = (xPos, yPos)
    wumpusStenches = []
    pitBreezes = []

    gold = False

    for key, value in worldInfo.items():
        if key == "wumpus":
            for coordinate in value:
                wumpusStenches.append((coordinate[0]+1, coordinate[1]))
                wumpusStenches.append((coordinate[0]-1, coordinate[1]))
                wumpusStenches.append((coordinate[0], coordinate[1]+1))
                wumpusStenches.append((coordinate[0], coordinate[1]-1))
        if key == "pit":
            for coordinate in value:
                pitBreezes.append((coordinate[0]+1, coordinate[1]))
                pitBreezes.append((coordinate[0]-1, coordinate[1]))
                pitBreezes.append((coordinate[0], coordinate[1]+1))
                pitBreezes.append((coordinate[0], coordinate[1]-1))
        if key == "gold":
            for coordinate in value:
                if coordinate[0] == playerLocation[0] and coordinate[1] == playerLocation[1]:
                    gold = True

    stench = wumpusStenches.__contains__(playerLocation)
    breeze = pitBreezes.__contains__(playerLocation)

    return stench, breeze, gold


class KBAgent:

    @staticmethod
    def recieveAndSavePrecepts():
        agentInfo = readASP('AgentPosition.gr')
        xPos = agentInfo['agent'][0][0]
        yPos = agentInfo['agent'][0][1]

        startingXPos = xPos

        world = readASP('WumpusWorldConfiguration.gr')
        printWorld(world,agentInfo)

        if startingXPos != xPos:
            f = open("AgentPosition.gr", "a")
            f.write("\nagent(" + str(xPos) + "," + str(yPos) + ").")
            f.close()

        worldInfo = readASP('WumpusWorldConfiguration.gr')
        stench, breeze, gold = generatePrecepts(agentInfo, worldInfo)

        if stench:
            print("Stench (" + str(xPos) + "," + str(yPos) + ")")
        if breeze:
            print("Breeze (" + str(xPos) + "," + str(yPos) + ")")
        if gold:
            print("Glitter (" + str(xPos) + "," + str(yPos) + ")")

    # @staticmethod
    # def decideOnNextAction():



if __name__ == "__main__":

    WumpusAgent = KBAgent
    while True:
        WumpusAgent.recieveAndSavePrecepts()
        # WumpusAgent.decideOnNextAction()
