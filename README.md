# Search-Methods-in-Packman
Uninformed and Informed Search Methods implementados en el clásico juego Pacman. El objetivo es que el agente de Pacman encuentre caminos a través de su mundo de laberintos, tanto para llegar a un lugar en particular como para recolectar alimentos de manera eficiente.
Se han construido algoritmos de búsqueda generales aplicandolos a los escenarios de Pacman.

## Uniformed Search Methods
- **Breadth-First Search** (Búsqueda en anchura):
    Implementado en el archivo search.py
    Uso: `py pacman.py -l mediumMaze -p SearchAgent -a fn=bfs` 
- **Depth-First Search** (Búsqueda en profundidad):
    Implementado en el archivo search.py
    Uso: `py pacman.py -l mediumMaze -p SearchAgent` 
- **Uniform-Cost Search** (Búsqueda de coste uniforme):
    Implementado en el archivo search.py
    Uso: `py pacman.py -l mediumDottedMaze -p StayEastSearchAgent`

## Iformed Search Methods
- **A* Search** (Búsqueda A*):
    Implementado en el archivo search.py
    Uso: `py pacman.py -l mediumDottedMaze -p StayEastSearchAgent`
- **Búsqueda de todas las esquinas**:
    Implementado en el archivo searchAgents.py
    Uso: `py pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem`
 - **Heurístico para buscar todas las esquinas**:
    Implementado en el archivo searchAgents.py
    Uso: `py pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5`
 - **Eating All The Dots** (Comiendo todos los puntos):
    Implementado en el archivo searchAgents.py
    Uso: `py pacman.py -l trickySearch -p AStarFoodSearchAgent`
  - **Suboptimal Search** (Búsqueda subóptima):
    Implementado en el archivo searchAgents.py
    Uso: `py pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5`
    


