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
    start_node = (problem.startingState(), '', 0)
    fringe = Stack()
    fringe.push(start_node)
    if (problem.isGoal(problem.startingState())):
        return
    visited = []
    while (fringe.__len__() != 0):
        curr_node = fringe.pop()
        curr_state = curr_node[0]
        if (problem.isGoal(curr_state)):
            tuple_result = tuple(map(str, curr_node[1].split(' ')))
            end_list = []
            for i in tuple_result:
                if (i != ''):
                    end_list.append(i)
            return end_list
        if (curr_state not in visited):
            visited.append(curr_state)
            for child_node in problem.successorStates(curr_state):
                child_state = child_node[0]
                child_node = list(child_node)
                if (child_state not in visited):
                    if (curr_node[1] != ''):
                        new_path = str(curr_node[1])
                        new_move = str(child_node[1])
                        new_path += ' ' + new_move
                        child_node[1] = new_path
                    fringe.push(child_node)

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first. [p 81]
    """
    # *** Your Code Here ***

    start_node = (problem.startingState(), '', 0)
    fringe = Queue()
    fringe.push(start_node)        # initialize queue with start node
    visited = []          # initialize list to check whether states have been visited
    visited.append(problem.startingState())   # initialize list with starting state
    while not fringe.isEmpty():       # while fringe is not empty, do the following
        curr_node = fringe.pop()
        curr_state = curr_node[0]
        for child_node in problem.successorStates(curr_state):    # check each child
            child_node = list(child_node)
            child_state = child_node[0]
            if problem.isGoal(child_state):  # if child state is goal, add child to visited
                tuple_result = tuple(map(str, curr_node[1].split(' ')))
                end_list = []
                for i in tuple_result:
                    if (i != ''):
                        end_list.append(i)
                end_list.append(child_node[1])
                return end_list
            else:                  # if child is not goal, append child if not seen before
                if (child_state not in visited):
                    if (curr_node[1] != ''):
                        new_path = str(curr_node[1])
                        new_move = str(child_node[1])
                        new_path += ' ' + new_move
                        child_node[1] = new_path
                    visited.append(child_state)
                    fringe.push(child_node)
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
