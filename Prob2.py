##################################################
# Name: Sophie Avery
# Collaborators:
# Estimate of time spent (hr): ~1
##################################################

def is_magic_square(array:list[list[int]]) -> bool:
    checksum = all([len(array[i]) == len(array) for i in range(len(array))])
    horizontal = [sum(array[i]) for i in range(len(array))]
    vertical = [sum([[array[i][j] for i in range(len(array))] for j in range(len(array))][i]) for i in range(len(array))]
    diagonal = [sum([array[i][i] for i in range(len(array))]) , sum([array[i][-i - 1] for i in range(len(array))])]
    all_sums = horizontal + vertical + diagonal
    for number in all_sums:
        if number != all_sums[0]:
            return False
    return True and checksum

small = [[8,1,6],[3,5,7],[4,9,2]]
large = [[2,16,13,3], [11,5,8,10], [7,9,12,6], [14,4,1,15]]
not_square = []
print(is_magic_square(small))
print(is_magic_square(large))
print(is_magic_square(not_square))

