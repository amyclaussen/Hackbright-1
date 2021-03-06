"""
Lists Lecture Exercise.
This project is a shopping list app.
We have a global list that will be our shopping list.
Make sure your code deals with upper and lower case.
"""
shopping_list = []


def reassign_list(list):
    shopping_list = list
    return shopping_list

def add_shopping_list(item):
    item = item.lower()
    if item not in shopping_list:
        shopping_list.append(item)
        print "%s has been added." % (item)
    else:
        print "This item %s already exists!" % (item)
    return sorted_shopping_list()


def sorted_shopping_list():
    shopping_list.sort()
    return shopping_list


def remove_item(item):
    item = item.lower()
    if item in shopping_list:
        shopping_list.remove(item)
        print "%s has been removed." % (item)
    else:
        print "%s was not on the list." % (item)
    return sorted_shopping_list()


print reassign_list(["Apple", "Orange"])
print sorted_shopping_list()

# TEST FUNCTIONS
# 1 - add 4 times to your shopping list
print add_shopping_list("apple")
print add_shopping_list("steak")
print add_shopping_list("beef")
print add_shopping_list("mustard")

# 2 - Add an item that is already in the list. what happens?
print add_shopping_list("apple")

# 3 - Remove an item on your list
print remove_item("apple")

# 4 - Remove an item that is not in the list. what happens?
print remove_item("chicken")
