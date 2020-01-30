from collections import deque

import pygame

from src.Settings import TILESIZE


class BreadthFirstSearch:

    def __init__(self, width, height, blacklisted):
        self.width = width
        self.height = height
        self.blacklisted = blacklisted
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # doesn't support diagonal paths, intentionally
        self.directions += [(1, 1), (-1, 1), (1, -1), (-1, -1)]

    def inBounds(self, node):
        # chained boundaries condition
        return 0 <= node[0] < self.width and 0 <= node[1] <= self.height

    def isValid(self, node):
        return node not in self.blacklisted  # checks if the node is unwalkable

    def findNeighbours(self, node):

        # LINQ-ish, inserts all of the directions to the node for filtering
        neighbours = []
        for direction in self.directions:
            neighbours.append((int(node[0]) + direction[0], int(node[1]) + direction[1]))

        # every other check, reverse directions, to get rid of horizontal/vertical only pathing
        # thus; we are not prioritizing the order of directions such as: right over left or down over top
        if (int(node[0]) + int(node[1])) % 2:
            neighbours.reverse()

        list(filter(self.inBounds, neighbours))
        list(filter(self.isValid, neighbours))
        return neighbours  # filters out


# especially useful for Tower Defence or Zombie games where the horde of enemies
# searches for the player as they have a pre-existing route
#   area: the map containing all tiles which are within a walkable path
#   start: the origin
def computePath(grid: BreadthFirstSearch, start, end):
    frontier = deque()
    frontier.append(start)

    path = []

    while len(frontier) > 0:
        currentTile = frontier.popleft()

        #  will exit the loop when we've already found a path
        if currentTile == end:
            break

        for neighbour in grid.findNeighbours(currentTile):
            nextIndex = (int(neighbour[0]), int(neighbour[1]))

            if nextIndex not in path:
                frontier.append(neighbour)
                waypoint = nextIndex  # (int(currentTile[0]) - int(neighbour[0]), int(currentTile[1]) - int(neighbour[1]))
                path.append(waypoint)  # direction
            # print(str(len(path)) + str(waypoint))

    return path
