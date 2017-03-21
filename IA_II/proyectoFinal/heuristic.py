"""
    Universidad Simon Bolivar
    CI-5438 - Inteligencia Artificial
    Edward Fernandez 10-11121
    Carlos Ferreira 11-10323
    Stefani Castellanos 11-11394

    Description:

"""
#
# board = [
# 			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# 			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# 			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# 			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# 			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# 			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# 			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# 			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# 			[0, 0, 0, 0, 4, 4, 0, 0, 0, 0],
# 			[0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
# 			[0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
# 			[0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
# 			[0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
# 			[0, 0, 7, 0, 0, 2, 0, 0, 0, 0],
# 			[0, 0, 7, 0, 0, 2, 2, 0, 0, 0],
# 			[0, 0, 7, 0, 2, 2, 1, 0, 0, 0],
# 			[0, 0, 7, 0, 0, 0, 1, 1, 0, 0],
# 			[7, 7, 7, 7, 0, 0, 1, 0, 0, 0],
# 			[7, 7, 7, 7, 0, 6, 6, 6, 6, 0],
# 			[1, 0, 0, 7, 7, 0, 4, 4, 0, 0],
# 			[1, 1, 0, 7, 7, 0, 4, 0, 0, 0],
# 			[1, 0, 6, 6, 6, 6, 4, 0, 0, 0],
#        ]

def isEmpty(cell):
    # print cell
    # print cell == 0
    return cell == 0

def isBlock(cell):
    return cell != 0

def aggregateHeight(board):
    totalHeight = 0
    for y in range(len(board[0])):
        for x in range(len(board)):
            if not isEmpty(board[x][y]):
                totalHeight += (len(board) - x)
                # print len(board) - x
                break

    return totalHeight

def completeLines(board):

    completedLines = 0
    for x in range(len(board)):
        if not (0 in board[x]):
            completedLines += 1

    return completedLines


def holes(board):
    """A hole is defined as an empty space below a block.
	The block doesn't have to be directly above the hole for it to count.
	This function identifies any holes and returns them as a [(x,y)]
	"""
    holes = []
    len_holes = 0
    block_in_col = False
    for x in range(len(board[0])):
        for y in range(len(board)):
            if block_in_col and isEmpty(board[y][x]):
                holes.append((x,y))
                len_holes += 1
            elif isBlock(board[y][x]):
                block_in_col = True
        block_in_col = False

    return len_holes

def bumpiness(board):
    bumpiness = 0
    old_height = 0
    new_height = 0
    for y in range(len(board[0])):
        for x in range(len(board)):
            if not isEmpty(board[x][y]):
                new_height = len(board) - x
                if y != 0:
                    bumpiness += abs(old_height - new_height)
                old_height = new_height
                break

    return bumpiness
