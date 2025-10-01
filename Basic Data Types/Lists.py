""" Consider a list (list = []). You can perform the following commands:

insert i e : Insert integer e at position i
print : Print the list
remove e : Delete the first occurrence of integer e
append e : Insert integer e at the end of the list
sort : Sort the list
pop : Pop the last element from the list
reverse : Reverse the list
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list. """

if __name__ == '__main__':
    N = int(input("Enter number:- "))
    the_list = []

    for _ in range(N):
        query = input().split()
        if query[0] == "print":
            print(the_list)
        elif query[0] == "insert":
            the_list.insert(int(query[1]), int(query[2]))
        elif query[0] == "remove":
            the_list.remove(int(query[1]))
        elif query[0] == "append":
            the_list.append(int(query[1]))
        elif query[0] == "sort":
            the_list = sorted(the_list)
        elif query[0] == "pop":
            the_list.pop()
        elif query[0] == "reverse":
            the_list.reverse()



