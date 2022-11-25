# search.py

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    ##util.raiseNotDefined()
    '''
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    '''

    pila = util.Stack()
    visitados = []
 
    start = problem.getStartState()
    if problem.isGoalState(start): # si el primer estado es el final, no procesar nada
        return []

    pila.push((start, [])) # añadir a la pila el estado (coordenadas) y el recorrido que se ha hecho hasta ese estado (al principio vacio)

    while not pila.isEmpty():
        actual, recorrido = pila.pop() # eliminar el primer elemento de la lista, obteniendo el estado y el recorrido para llegar a ella.
             
        if actual not in visitados:  # si no ha sido visitado

            visitados.append(actual) # el nodo se ha visitado

            if problem.isGoalState(actual): # si el nodo actual es el resultado, se acaba y se devuelve el recorrido hasta ese estado
                return recorrido
            else:
                    
                vecinos = problem.getSuccessors(actual)
                for koor, mugi, kostua in vecinos:      # recorrer los sucesores                  
                    siguiente = recorrido + [mugi]      # añadir el movimiento para llegar a los hijos (para cada uno sera distinto)    
                    pila.push((koor, siguiente))

    return []
    




def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    cola = util.Queue()
    visitados = []

    start = problem.getStartState()
    if problem.isGoalState(start):
        return []
        
    cola.push((start, []))

    while not cola.isEmpty():
        actual, recorrido = cola.pop()

        if actual not in visitados:

            visitados.append(actual)

            if problem.isGoalState(actual):
                return recorrido
            else:
                    
                vecinos = problem.getSuccessors(actual)
                for koor, mugi, kostua in vecinos:      
                    siguiente = recorrido + [mugi]
                    cola.push((koor, siguiente))

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    colaPrioridad = util.PriorityQueue()
    visitados = []

    start = problem.getStartState()
    if problem.isGoalState(start):
        return []

    colaPrioridad.push((start, [], 0), 0)

    while not colaPrioridad.isEmpty():
        actual, recorrido, prioridad =  colaPrioridad.pop()

        if actual not in visitados:
            visitados.append(actual)

            if problem.isGoalState(actual):
                return recorrido
            else:
                
                vecinos = problem.getSuccessors(actual)
                for koor, mugi, kostua in vecinos:               
                    nuevaPrioridad = prioridad + kostua
                    siguiente = recorrido + [mugi]            
                    colaPrioridad.push((koor, siguiente, nuevaPrioridad), nuevaPrioridad)

    return []
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    colaPrioridad = util.PriorityQueue()
    visitados = []

    start = problem.getStartState()
    if problem.isGoalState(start):
        return []

    colaPrioridad.push((start, [], 0), 0)

    while not colaPrioridad.isEmpty():
        actual, recorrido, prioridad =  colaPrioridad.pop()

        if actual not in visitados:
            
            visitados.append(actual)

            if problem.isGoalState(actual):
                return recorrido
            else:

                vecinos = problem.getSuccessors(actual)
                for koor, mugi, kostua in vecinos:                  
                    nuevaPrioridad = prioridad + kostua
                    siguiente = recorrido + [mugi]

                    heuristico = nuevaPrioridad + heuristic(koor, problem)
                    
                    colaPrioridad.push((koor, siguiente, nuevaPrioridad), heuristico)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
