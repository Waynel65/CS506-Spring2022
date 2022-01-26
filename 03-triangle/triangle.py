
def read_triangle(filepath):
    """
        takes a filepath and returns a triangle
        represented as a list of list
    """
    # open(filepath, "w+") ## w+ creates a new filepath if the specified path does not exist already
                         ## not a great idea cuz it does not return an error
    
    triangle = []
    with open(filepath, "r") as f:
        lines = f.readlines()
        for line in lines:
            triangle.append(
                [int(char) for char in line.split(" ")]
            )
        

    return triangle


def do_fold(curr_level, next_level):
    """
        returns a map
    """

    # curr_level = triangle[0]
    # next_level = triangle[1]

    ## a trick of mimicing going to right and left
    right_options = [0] + curr_level
    left_options = curr_level + [0]

    sum_from_the_right = zip(next_level, right_options) ## make the iteratables tuples
    sum_from_the_right = map(lambda x: x[0] + x[1], sum_from_the_right)

    sum_from_the_left = zip(next_level, left_options)
    sum_from_the_left = map(lambda x: x[0] + x[1], sum_from_the_left)

    max_fold_sum = list(map(lambda x : max(x), zip(sum_from_the_left, sum_from_the_right)))

    return max_fold_sum

def fold(triangle):
    curr_level = triangle[0]

    for level in range(1, len(triangle)):
        next_level = triangle[level]
        curr_level = do_fold(curr_level, next_level)

    return max(curr_level)


## top-down approach: 
print(fold(read_triangle("./triangle.txt")))