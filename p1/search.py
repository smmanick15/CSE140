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

    print("Start: %s" % (str(problem.startingState())))
    print("Is the start a goal?: %s" % (problem.isGoal(problem.startingState())))
    print("Start's successors: %s" % (problem.successorStates(problem.startingState())))
    print(problem.successorStates(problem.startingState()))

    # *** Your Code Here ***

    start_node = (problem.startingState(), '', 0)
    print("to make sure we initialized the start node right... let's try printing it!!!\n\n\n")
    print(start_node)
    frontier = Queue()
    i = 0
    frontier.push(start_node)
    
    reached = []
    reached.append(problem.startingState())
    recentNodes = Stack()
    recentNodes.push(start_node)
    foundGoal = False

    while not frontier.isEmpty():
        node = frontier.pop()
        print("the node we just popped is: ", node)
        #i = 0
        state = node[0]
        print(state)
        print(problem.successorStates(state))
        print(frontier.__len__())
        for child in problem.successorStates(state):
            goal = child
            childState = child[0]
            print("inside for loop, printing child: ", childState)
            if problem.isGoal(childState):
                print("did we ever find the goal...? YES WE DIDDDDDD LET'S CELEBRATE")
                print("let's make sure we have the right goal though...: ", child)
                print("what are the successor states of this child?, see below\n")
                print(problem.successorStates(childState))
                recentNodes.push(child)
                foundGoal = True
                break
            else:
                if (childState not in reached):
                    print("we did not find", childState, "in reached")
                    reached.append(childState)
                    frontier.push(child)
                    recentNodes.push(child)
        if (foundGoal == True):
            break


    print("\n\n\nabout to print s after exiting graph traversal: ", childState)
    print(reached)
    print("lets look at the length of the recent nodes visited: ", recentNodes.__len__())

    back_state = childState
    actions = []
    
    while (back_state != problem.startingState()):
        compare_node = recentNodes.pop()
        print("this is the node we are comparing ", back_state, "to: ", compare_node)
        print(problem.successorStates(back_state))
        if (back_state == compare_node[0]):
            actions.append(compare_node[1])
        found_next = False
        for child in problem.successorStates(back_state):
            if (child[0] == compare_node[0]):       #check if successor state is valid
                print("YAY! We found a valid state\n")
                back_state = compare_node[0]
                if (compare_node[1] != ''):
                    actions.append(compare_node[1])
                found_next = True
                break
    
    actions.reverse()
    print("printing returned list of actions: ", actions)
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
