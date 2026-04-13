food = {"pasta", "burger", "hotdog", "pizza"}
print(food)

food.discard("pasta")
print(food)

food.remove("burger")
print(food)

# The next two lines try to remove an item that isn’t in the set!
food.discard("pasta")  # this will not report an error
food.remove("pasta")   # this will report an error
