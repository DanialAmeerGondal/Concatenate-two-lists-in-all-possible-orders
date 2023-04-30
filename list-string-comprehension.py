list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# We're given two lists, and we want to make them in the form:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

# So what we can do is use a nested loop and iterate over each lists' items. 
# For each iteration of the outer loop (x) we'll add the inner loop (y) until it's exhausted. It will do this until the outer loop has finished, and each
# time it will add the result in a list. 

added = [x + y for x in list1 for y in list2]

print(added)
