# program to split lists

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 2

# splits the list
def split_ls(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i+chunk_size]


print(list(split_ls(my_list, chunk_size)))