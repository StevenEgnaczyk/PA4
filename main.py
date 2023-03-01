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

def generatePrecepts(agentInfo, worldInfo):

    precepts = {}

    xPos = agentInfo['agent'][0][0]
    yPos = agentInfo['agent'][0][1]

    playerLocation = (xPos, yPos)
    wumpusStenches = []
    pitBreezes = []

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

    print(playerLocation)
    print(wumpusStenches)
    stench = wumpusStenches.__contains__(playerLocation)
    breeze = pitBreezes.__contains__(playerLocation)
    print(stench)
    print(breeze)


class KBAgent:

    @staticmethod
    def recieveAndSavePrecepts():
        agentInfo = readASP('AgentPosition.gr')
        xPos = agentInfo['agent'][0][0]
        yPos = agentInfo['agent'][0][1]

        startingXPos = xPos

        if startingXPos != xPos:
            f = open("AgentPosition.gr", "a")
            f.write("\nagent(" + str(xPos) + "," + str(yPos) + ").")
            f.close()

        worldInfo = readASP('WumpusWorldConfiguration.gr')
        generatePrecepts(agentInfo, worldInfo)

    @staticmethod
    def decideOnNextAction():
        print("Penis Again")


if __name__ == "__main__":

    WumpusAgent = KBAgent
    while True:
        WumpusAgent.recieveAndSavePrecepts()
        WumpusAgent.decideOnNextAction()
