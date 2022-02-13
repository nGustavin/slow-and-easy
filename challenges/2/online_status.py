# Online status

# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# statuses = {
#     "Alice": "online",
#     "Bob": "offline",
#     "Eve": "online",
# }

# In this case, the number of people online is 2.

# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

# Your function should return the number of people who are online.

def online_count(statuses: dict) -> int:
    """
    Return the amount of online users on a list
    """
    acc = 0
    for position in statuses:
        if statuses[position] == "online":
            acc += 1
        else:
            pass
    return acc