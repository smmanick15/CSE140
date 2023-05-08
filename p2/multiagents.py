import random

from pacai.core import distance
from pacai.agents.base import BaseAgent
from pacai.agents.search.multiagent import MultiAgentSearchAgent

class ReflexAgent(BaseAgent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.
    You are welcome to change it in any way you see fit,
    so long as you don't touch the method headers.
    """

    def __init__(self, index, **kwargs):
        super().__init__(index, **kwargs)

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        `ReflexAgent.getAction` chooses among the best options according to the evaluation function.

        Just like in the previous project, this method takes a
        `pacai.core.gamestate.AbstractGameState` and returns some value from
        `pacai.core.directions.Directions`.
        """

        # Collect legal moves.
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions.
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best.

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current `pacai.bin.pacman.PacmanGameState`
        and an action, and returns a number, where higher numbers are better.
        Make sure to understand the range of different values before you combine them
        in your evaluation function.
        """

        successorGameState = currentGameState.generatePacmanSuccessor(action)

        # Useful information you can extract.
        # newPosition = successorGameState.getPacmanPosition()
        # oldFood = currentGameState.getFood()
        # newGhostStates = successorGameState.getGhostStates()
        # newScaredTimes = [ghostState.getScaredTimer() for ghostState in newGhostStates]

        # *** Your Code Here ***

        oldFood = currentGameState.getFood()
        position1 = successorGameState.getPacmanPosition()
        heuristic = 99999999999
        for food_coord in oldFood.asList():
            manhattan = distance.manhattan(position1, food_coord)
            if (manhattan < heuristic):  # if manhattan distance is greater than previous:
                heuristic = manhattan

        ghost_heuristic = 999999999
        for ghost in successorGameState.getGhostPositions():
            ghost_dist = distance.manhattan(position1, ghost)
            if (ghost_dist < ghost_heuristic):
                ghost_heuristic = ghost_dist

        if (heuristic != 0):
            if (ghost_heuristic != 0):
                return (successorGameState.getScore() + (6 * (1 / heuristic))
                        - (12 * (1 / ghost_heuristic)))
            else:
                return successorGameState.getScore() + 6 * (1 / heuristic)
        else:
            if (ghost_heuristic != 0):
                return (successorGameState.getScore() - 12 * (1 / ghost_heuristic))
            else:
                return successorGameState.getScore()

class MinimaxAgent(MultiAgentSearchAgent):
    """
    A minimax agent.

    Here are some method calls that might be useful when implementing minimax.

    `pacai.core.gamestate.AbstractGameState.getNumAgents()`:
    Get the total number of agents in the game

    `pacai.core.gamestate.AbstractGameState.getLegalActions`:
    Returns a list of legal actions for an agent.
    Pacman is always at index 0, and ghosts are >= 1.

    `pacai.core.gamestate.AbstractGameState.generateSuccessor`:
    Get the successor game state after an agent takes an action.

    `pacai.core.directions.Directions.STOP`:
    The stop direction, which is always legal, but you may not want to include in your search.

    Method to Implement:

    `pacai.agents.base.BaseAgent.getAction`:
    Returns the minimax action from the current gameState using
    `pacai.agents.search.multiagent.MultiAgentSearchAgent.getTreeDepth`
    and `pacai.agents.search.multiagent.MultiAgentSearchAgent.getEvaluationFunction`.
    """

    def __init__(self, index, **kwargs):
        super().__init__(index, **kwargs)

    def getAction(self, gameState):
        depth_param = MultiAgentSearchAgent.getTreeDepth(self)
        legalMoves = gameState.getLegalActions(self.index)
        max_score = float('-inf')
        final_action = ''
        for action in legalMoves:
            if (action == 'Stop'):
                continue
            else:
                new_score = self.value(self.index, depth_param,
                                       gameState.generateSuccessor(self.index, action))
                if (new_score > max_score):
                    max_score = new_score
                    final_action = action
        # print("for action: ", final_action)
        # print("max score: ", max_score)
        return final_action

    def value(self, agentIndex, depth, gameState):
        if (gameState.isWin()) or (gameState.isLose()) or (depth <= 0):
            score = gameState.getScore()
            return score

        next_agent = (agentIndex + 1) % gameState.getNumAgents()
        if (next_agent == 0):
            depth = depth - 1
            return self.maxValue(agentIndex, depth, gameState)
        else:
            return self.minValue(agentIndex, depth, gameState)

    def maxValue(self, agentIndex, depth, gameState):
        if (gameState.isWin()) or (gameState.isLose()) or (depth <= 0):
            return self.getEvaluationFunction()(gameState)

        value = float('-inf')
        next_ag = agentIndex + 1
        new_ind = next_ag % gameState.getNumAgents()

        for action in gameState.getLegalActions(new_ind):
            if (action == 'Stop'):
                continue
            else:
                s = gameState.generateSuccessor(new_ind, action)
                value = max(value, self.value(new_ind, depth, s))
        return value

    def minValue(self, agentIndex, depth, gameState):
        if (gameState.isWin()) or (gameState.isLose()) or (depth <= 0):
            return self.getEvaluationFunction()(gameState)

        value = float('inf')
        next_ag = agentIndex + 1
        new_ind = next_ag % gameState.getNumAgents()

        for action in gameState.getLegalActions(new_ind):
            if (action == 'Stop'):
                continue
            else:
                s = gameState.generateSuccessor(new_ind, action)
                value = min(value, self.value(new_ind, depth, s))
        return value

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    A minimax agent with alpha-beta pruning.

    Method to Implement:

    `pacai.agents.base.BaseAgent.getAction`:
    Returns the minimax action from the current gameState using
    `pacai.agents.search.multiagent.MultiAgentSearchAgent.getTreeDepth`
    and `pacai.agents.search.multiagent.MultiAgentSearchAgent.getEvaluationFunction`.
    """

    def __init__(self, index, **kwargs):
        super().__init__(index, **kwargs)

    def getAction(self, gameState):
        depth_p = MultiAgentSearchAgent.getTreeDepth(self)
        legalMoves = gameState.getLegalActions(self.index)
        max_score = float('-inf')
        final_action = ''
        for action in legalMoves:
            if (action == 'Stop'):
                continue
            else:
                new_score = self.value(self.index, depth_p,
                                       gameState.generateSuccessor(self.index, action),
                                       float('-inf'), float('inf'))
                if (new_score > max_score):
                    max_score = new_score
                    final_action = action
        # print("for action: ", final_action)
        # print("max score: ", max_score)
        return final_action

    def value(self, agentIndex, depth, gameState, alpha, beta):
        if (gameState.isWin()) or (gameState.isLose()) or (depth <= 0):
            score = gameState.getScore()
            return score

        next_agent = (agentIndex + 1) % gameState.getNumAgents()
        if (next_agent == 0):
            depth = depth - 1
            return self.maxValue(agentIndex, depth, gameState, alpha, beta)
        else:
            return self.minValue(agentIndex, depth, gameState, alpha, beta)

    def maxValue(self, agentIndex, depth, gameState, alpha, beta):
        if (gameState.isWin()) or (gameState.isLose()) or (depth <= 0):
            return self.getEvaluationFunction()(gameState)

        value = float('-inf')
        next_ag = agentIndex + 1
        new_ind = next_ag % gameState.getNumAgents()

        for action in gameState.getLegalActions(new_ind):
            if (action == 'Stop'):
                continue
            else:
                s = gameState.generateSuccessor(new_ind, action)
                value = max(value, self.value(new_ind, depth, s, alpha, beta))

                alpha = max(alpha, value)
                if (beta <= alpha):
                    break
        return value

    def minValue(self, agentIndex, depth, gameState, alpha, beta):
        if (gameState.isWin()) or (gameState.isLose()) or (depth <= 0):
            return self.getEvaluationFunction()(gameState)

        value = float('inf')
        next_ag = agentIndex + 1
        new_ind = next_ag % gameState.getNumAgents()

        for action in gameState.getLegalActions(new_ind):
            if (action == 'Stop'):
                continue
            else:
                s = gameState.generateSuccessor(new_ind, action)
                value = min(value, self.value(new_ind, depth, s, alpha, beta))

                beta = min(beta, value)
                if (beta <= alpha):
                    break
        return value

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
    An expectimax agent.

    All ghosts should be modeled as choosing uniformly at random from their legal moves.

    Method to Implement:

    `pacai.agents.base.BaseAgent.getAction`:
    Returns the expectimax action from the current gameState using
    `pacai.agents.search.multiagent.MultiAgentSearchAgent.getTreeDepth`
    and `pacai.agents.search.multiagent.MultiAgentSearchAgent.getEvaluationFunction`.
    """

    def __init__(self, index, **kwargs):
        super().__init__(index, **kwargs)

    def getAction(self, gameState):
        depth_param = MultiAgentSearchAgent.getTreeDepth(self)
        legalMoves = gameState.getLegalActions(self.index)
        max_score = float('-inf')
        final_action = ''
        for action in legalMoves:
            if (action == 'Stop'):
                continue
            else:
                new_score = self.value(self.index, depth_param,
                                       gameState.generateSuccessor(self.index, action))
                if (new_score > max_score):
                    max_score = new_score
                    final_action = action
        # print("for action: ", final_action)
        # print("max score: ", max_score)
        return final_action

    def value(self, agentIndex, depth, gameState):
        if (gameState.isWin()) or (gameState.isLose()) or (depth <= 0):
            score = gameState.getScore()
            return score

        next_agent = (agentIndex + 1) % gameState.getNumAgents()
        if (next_agent == 0):
            depth = depth - 1
            return self.maxValue(agentIndex, depth, gameState)
        else:
            return self.expValue(agentIndex, depth, gameState)

    def maxValue(self, agentIndex, depth, gameState):
        if (gameState.isWin()) or (gameState.isLose()) or (depth <= 0):
            return self.getEvaluationFunction()(gameState)

        value = float('-inf')
        next_ag = agentIndex + 1
        new_ind = next_ag % gameState.getNumAgents()

        for action in gameState.getLegalActions(new_ind):
            if (action == 'Stop'):
                continue
            else:
                s = gameState.generateSuccessor(new_ind, action)
                value = max(value, self.value(new_ind, depth, s))
        return value

    def expValue(self, agentIndex, depth, gameState):
        if (gameState.isWin()) or (gameState.isLose()) or (depth <= 0):
            return self.getEvaluationFunction()(gameState)

        next_ag = agentIndex + 1
        new_ind = next_ag % gameState.getNumAgents()

        value_list = []
        for action in gameState.getLegalActions(new_ind):
            if (action == 'Stop'):
                continue
            else:
                s = gameState.generateSuccessor(new_ind, action)
                value_list.append(self.value(new_ind, depth, s))

        total = 0
        average = 0
        for val in value_list:
            total = total + val

        average = total / len(value_list)
        return average

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable evaluation function.

    DESCRIPTION: <write something here so we know what you did>
    """

    # Useful information you can extract.
    # newPosition = successorGameState.getPacmanPosition()
    # oldFood = currentGameState.getFood()
    # newGhostStates = successorGameState.getGhostStates()
    # newScaredTimes = [ghostState.getScaredTimer() for ghostState in newGhostStates]

    # *** Your Code Here ***

    oldFood = currentGameState.getFood()
    position1 = currentGameState.getPacmanPosition()
    heuristic = float('inf')
    for food_coord in oldFood.asList():
        manhattan = distance.manhattan(position1, food_coord)
        if (manhattan < heuristic):  # if manhattan distance is greater than previous:
            heuristic = manhattan

    ghost_heuristic = float('inf')
    for ghost in currentGameState.getGhostPositions():
        ghost_dist = distance.manhattan(position1, ghost)
        if (ghost_dist < ghost_heuristic):
            ghost_heuristic = ghost_dist

    if (heuristic != 0):
        if (ghost_heuristic != 0):
            return (currentGameState.getScore() + 7 * (1 / heuristic) - 14 * (1 / ghost_heuristic))
        else:
            return currentGameState.getScore() + 7 * (1 / heuristic)
    else:
        if (ghost_heuristic != 0):
            return (currentGameState.getScore() - 14 * (1 / ghost_heuristic))
        else:
            return currentGameState.getScore()

    return currentGameState.getScore()

class ContestAgent(MultiAgentSearchAgent):
    """
    Your agent for the mini-contest.

    You can use any method you want and search to any depth you want.
    Just remember that the mini-contest is timed, so you have to trade off speed and computation.

    Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
    just make a beeline straight towards Pacman (or away if they're scared!)

    Method to Implement:

    `pacai.agents.base.BaseAgent.getAction`
    """

    def __init__(self, index, **kwargs):
        super().__init__(index, **kwargs)
