from pacai.util.stack import Stack
from pacai.util.queue import Queue
from pacai.util.priorityQueue import PriorityQueue

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
    fringe.push(start_node)   # initialize fringe with start node
    if (problem.isGoal(problem.startingState())):   # check if start is goal
        return
    visited = []
    while (fringe.__len__() != 0):   # while fringe not empty, traverse through graph
        curr_node = fringe.pop()
        curr_state = curr_node[0]
        if (problem.isGoal(curr_state)):   # if state is goal, return path list
            return curr_node[1]
        if (curr_state not in visited):   # if state is new:
            visited.append(curr_state)    # add to visited nodes list
            for child_node in problem.successorStates(curr_state):
                child_state = child_node[0]
                child_node = list(child_node)
                if (child_state not in visited):   # if child is new:
                    action_str = child_node[1]     # update action path
                    child_node[1] = []
                    for act in curr_node[1]:
                        child_node[1].append(act)
                    child_node[1].append(action_str)
                    fringe.push(child_node)   # push child to fringe

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first. [p 81]
    """
    # *** Your Code Here ***
    start_node = (problem.startingState(), [], 0)
    fringe = Queue()
    fringe.push(start_node)   # initialize fringe with start node
    if (problem.isGoal(problem.startingState())):   # check if start is goal
        return
    visited = []
    while (fringe.__len__() != 0):   # while fringe not empty, traverse through graph
        curr_node = fringe.pop()
        curr_state = curr_node[0]
        if (problem.isGoal(curr_state)):   # if state is goal, return path list
            return curr_node[1]
        if (curr_state not in visited):   # if state is new:
            visited.append(curr_state)    # add to visited nodes list
            for child_node in problem.successorStates(curr_state):
                child_state = child_node[0]
                child_node = list(child_node)
                if (child_state not in visited):   # if child is new:
                    action_str = child_node[1]     # update action path
                    child_node[1] = []
                    for act in curr_node[1]:
                        child_node[1].append(act)
                    child_node[1].append(action_str)
                    fringe.push(child_node)   # push child to fringe

def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """

    start_node = (problem.startingState(), [], 0)
    fringe = PriorityQueue()
    fringe.push(start_node, 1)   # initialize fringe with start node
    if (problem.isGoal(problem.startingState())):   # check if start is goal
        return
    visited = []
    while (fringe.__len__() != 0):   # while fringe not empty, traverse through graph
        curr_node = fringe.pop()
        curr_state = curr_node[0]
        if (problem.isGoal(curr_state)):   # if state is goal, return path list
            return curr_node[1]
        if (curr_state not in visited):   # if state is new:
            visited.append(curr_state)    # add to visited nodes list
            for child_node in problem.successorStates(curr_state):
                child_state = child_node[0]
                child_node = list(child_node)
                if (child_state not in visited):   # if child is new:
                    action_str = child_node[1]     # update action path
                    child_node[1] = []
                    for act in curr_node[1]:
                        child_node[1].append(act)
                    child_node[1].append(action_str)
                    # calculate cost of path (use as fringe priority), push to fringe
                    act_cost = problem.actionsCost(child_node[1])
                    fringe.push(child_node, act_cost)   # push child to fringe

    print("failed search")
    return None


def aStarSearch(problem, heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """

    # *** Your Code Here ***
    start_node = (problem.startingState(), [], problem.actionsCost([]))
    fringe = PriorityQueue()
    # initialize fringe with start node
    fringe.push(start_node, heuristic(problem.startingState(), problem))
    if (problem.isGoal(problem.startingState())):   # check if start is goal
        return
    visited = []

    while (fringe.__len__() != 0):   # while fringe not empty, traverse through graph
        curr_node = fringe.pop()
        curr_state = curr_node[0]
        if (problem.isGoal(curr_state)):   # if state is goal, return path list
            return curr_node[1]
        if (curr_state not in visited):   # if state is new:
            visited.append(curr_state)    # add to visited nodes list
            for child_node in problem.successorStates(curr_state):
                child_state = child_node[0]
                child_node = list(child_node)
                if (child_state not in visited):   # if child is new:
                    action_str = child_node[1]      # update action path
                    child_node[1] = []
                    for act in curr_node[1]:
                        child_node[1].append(act)
                    child_node[1].append(action_str)
                    # calculate cost of path (use as fringe priority), push to fringe
                    act_cost = problem.actionsCost(child_node[1])
                    fringe.push(child_node, act_cost + heuristic(child_state, problem))

    print("failed search")
    return None

    raise NotImplementedError()
