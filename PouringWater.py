def solution(X, Y, goal, start=(0, 0)):
    """
    X and Y are the capacity of the glasses.
    (x, y) is current fill level and represents a state.
    The goal is a level that can in either glass.

    Start at start state and follow successors until reach goal.
    Keep track of frontier and previously explored.
    Fail when no frontier remains.
    """

    if goal in start:
        return [start]
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        x, y = path[-1] # Last state in the first path of the frontier
        for state, action in successors(x, y, X, Y).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if goal in state:
                    return path2
                else:
                    frontier.append(path2)
    return []

def successors(x, y, X, Y):
    """
    Current level of glasses: x, y
    Full capacity of glasses: X, Y

    Returns a dict of {state:action} pairs
    describing what can be reached from the
    current (x, y) state, and how.
    """
    assert x<= X and y <= Y # state is <= capacity
    return {
        ((0, y+x) if y+x<=Y else (x-(Y-y), y+(Y-y))): 'X->Y',
        ((x+y, 0) if x+y<=X else (x+(X-x), y-(X-x))): 'X<-Y',
        (X, y): 'fill X',
        (x, Y): 'fill Y',
        (0, y): 'empty X',
        (x, 0): 'empty Y',
    }



result = solution(6, 15, 9)
print("\n".join(str(i) for i in result))



