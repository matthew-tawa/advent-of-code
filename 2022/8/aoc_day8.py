from math import ceil
from math import trunc

#f = open('8\\forest.txt', 'r')
f = open('8\\input.txt', 'r')

forest = None
forest_cols = 0
forest_rows = 0


def build_forest():
    global f, forest, forest_cols, forest_rows

    # creating the forest as one string
    forest_str = f.readline()[0:-1]
    forest_cols = len(forest_str)
    forest_rows = 1

    input = f.readline()
    alive = True
    while alive:
        forest_str += input[0:forest_cols]
        forest_rows += 1

        input = f.readline()
        alive = (input != "")

    f.close()

    # converting the forst string to a list
    forest = list(forest_str)


# count the number of trees visible from the perimiter
def main1():
    global forest, forest_cols, forest_rows

    visible_tree_count = 0

    # looping over each item to determine visibility
    for pos, tree in enumerate(forest):

        # if tree is in first of last column, its visible
        if (pos % forest_rows == 0 or (pos+1) % forest_rows == 0):
            visible_tree_count += 1
                
        # if tree is in first of last row, its visible
        elif (pos < forest_cols or pos > len(forest)-forest_cols):
            visible_tree_count += 1

        # otherwise we are inside forest and need to check
        else:
            visible_from_N = max(set(forest[pos%forest_rows:pos:forest_cols])) < tree
            visible_from_S = max(set(forest[pos+forest_cols::forest_cols]))  < tree
            visible_from_E = max(set(forest[pos+1:ceil(pos/forest_cols)*forest_cols]))  < tree
            visible_from_W = max(set(forest[trunc(pos/forest_cols)*forest_cols:pos]))  < tree
            visible = visible_from_N or visible_from_S or visible_from_E or visible_from_W

            if (visible):
                visible_tree_count += 1
    
    print("\nqty trees visible from perimiter: " + str(visible_tree_count) + "\n")



# find the highest scenic score in the forest
def main2():
    global forest, forest_cols, forest_rows

    highest_scenic_score = 0

    # looping over each item to determine scenic score
    for pos, tree in enumerate(forest):

        tree_is_first_or_last_col = (pos % forest_rows == 0 or (pos+1) % forest_rows == 0)
        tree_is_first_or_last_row = (pos < forest_cols or pos > len(forest)-forest_cols)
        
        # only care about scenic score if not on perimiter (since perimeter scenic score is 0)
        if not (tree_is_first_or_last_col or tree_is_first_or_last_row):
            trees_N = list(forest[pos%forest_rows:pos:forest_cols])
            trees_S = list(forest[pos+forest_cols::forest_cols])
            trees_E = list(forest[pos+1:ceil(pos/forest_cols)*forest_cols])
            trees_W = list(forest[trunc(pos/forest_cols)*forest_cols:pos])

            # directional_scenic_score expects arrays ordered from current tree outwards
            # due to way these two are constructed, need to reverse them
            trees_N.reverse()
            trees_W.reverse()

            current_scenic_score = 1
            current_scenic_score *= directional_scenic_score(tree, trees_N)
            current_scenic_score *= directional_scenic_score(tree, trees_S)
            current_scenic_score *= directional_scenic_score(tree, trees_E)
            current_scenic_score *= directional_scenic_score(tree, trees_W)

            if (current_scenic_score > highest_scenic_score):
                highest_scenic_score = current_scenic_score



    print("\nmax scnenic score: " + str(highest_scenic_score) + "\n")

# returns a directional scenic score
# pos -> current position to evaluate
# trees_in_dir -> list of trees to check (closest tree first in list)
def directional_scenic_score(mytree: int, trees_in_dir) -> int:
    visible_trees_from_pos = 0

    for tree in trees_in_dir:
        visible_trees_from_pos += 1

        if int(mytree) <= int(tree):
            break

    return visible_trees_from_pos



# methodology:
# get unique list with all trees to the right, left, top, and bottom
# for each tree height in the unique list, check if any are larger or equal to current tree
# if any are larger or equal, cant be seen from that direction



build_forest()
main1()
main2()