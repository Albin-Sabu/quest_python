# Albin Sabu Assesment Problem Name:  Maximum element in stack problem


def query_function(number_of_queries,stack):
    for i in range(number_of_queries):    
        request = [int(query) for query in input().split(' ')]
        if request[0] == 1:
            stack.append(request[1])
        elif request[0] == 2:
            del stack[-1]
        else:
            a = max(stack)
            print(a)


number_of_queries = int(input("Enter the number of queries in stack: "))
stack = [0]


query_function(number_of_queries,stack)
