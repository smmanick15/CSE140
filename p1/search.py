from pacai.util.stack import Stack
from pacai.util.queue import Queue

"""
In this file, you will implement generic search algorithms which are called by Pacman agents.
"""

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 85].

    Your search algorithm needs to return a list of actions that reaches the goal.
    Make sure to implement a graph search algorithm [Fig. 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    ```
    print("Start: %s" % (str(problem.startingState())))
    print("Is the start a goal?: %s" % (problem.isGoal(problem.startingState())))
    print("Start's successors: %s" % (problem.successorStates(problem.startingState())))
    ```
    """

    
    # *** Your Code Here ***
    raise NotImplementedError()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first. [p 81]
    """

    # print("Start: %s" % (str(problem.startingState())))
    # print("Is the start a goal?: %s" % (problem.isGoal(problem.startingState())))
    # print("Start's successors: %s" % (problem.successorStates(problem.startingState())))
    # print(problem.successorStates(problem.startingState()))

    # *** Your Code Here ***

    start_node = (problem.startingState(), '', 0)
    frontier = Queue()
    frontier.push(start_node)        # initialize queue with start node
    
    reached = []          # initialize list to check whether states have been visited    
    reached.append(problem.startingState()) # initialize list with starting state
    recentNodes = Stack()   # initialize stack used to track nodes from goal state to origin state
    recentNodes.push(start_node)
    foundGoal = False

    while not frontier.isEmpty():       # while fringe is not empty, do the following
        node = frontier.pop()
        state = node[0]
        for child in problem.successorStates(state):    # check each child node of parent node
            goal = child
            childState = child[0]
            if problem.isGoal(childState):     # if child state is goal, push child to visited nodes stack and break
                recentNodes.push(child)
                foundGoal = True
                break
            else:                              # if child is not goal, append child if it is a new state (not seen before)
                if (childState not in reached):
                    reached.append(childState)
                    frontier.push(child)
                    recentNodes.push(child)
        if (foundGoal == True):
            break

    back_state = childState        
    actions = []                    # list of actions to return
    
    while (back_state != problem.startingState()):  # while the current state is not the origin, do:
        compare_node = recentNodes.pop()
        if (back_state == compare_node[0]):         # if current state is the last node visited, add action
            actions.append(compare_node[1])
        found_next = False
        for child in problem.successorStates(back_state):
            if (child[0] == compare_node[0]):       # check if successor state is valid
                back_state = compare_node[0]        # if valid, set current state to successor state
                if (compare_node[1] != ''):         # add action to list of results
                    actions.append(compare_node[1])
                found_next = True
                break
    
    actions.reverse()               # reverse order of action steps
    return actions

    # raise NotImplementedError()

def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """

    # *** Your Code Here ***
    raise NotImplementedError()

def aStarSearch(problem, heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """

    # *** Your Code Here ***
    raise NotImplementedError()
