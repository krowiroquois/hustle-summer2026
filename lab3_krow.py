# Krow Iroquois | Lab 3 | Green

#1
username = "@snowlicorice"
# Predict: 13 characters
#print(len(username))
# Answer: yes, len did count all characters including symbols

#2
#print(username[1])
#print(username[12])
# Predict: "s" and "e"
# Answer: because indexes start from the number 0, not the number 1

#3
welcome = "Welcome to Loop,"
message = welcome + " " + username + "!"
# Predict: yes
#print(f"Welcome to Loop, {username}!")
#print(message)
# Answer: f-string felt a lot easier because it required much less typing

#4
#username[0] = "X"
#print(username[0])
#TypeError: 'str' object does not support item assignment

#5
feed = ["i love cats", "i love taco salad", "i love anime"]
#print(len(feed))
#print(feed[0])
# Predict: the number 3 will print; the caption "i love cats" will print
# Answer: i used index 0 because 0 is the very first number in an index, and "i love cats" is the first post

#6
feed.append("i love the color yellow")
# Predict: index 3
#print(feed)
# Answer: because indexes start from the number 0 and there are already 3 existing posts;
# therefore, the new post would be at index 3.

#7
feed.pop(0)
feed.sort()
#print(feed)
# Predict: "i love cats" gets removed. the order then changes to "i love anime", "i love taco salad",
# and then "i love the color yellow"
# Answer: pop(0) got rid of the very first index, and sort listed every index in alphabetical order.

#8
profile = {"username": "snowlicorice",
"followers": 5000,
"verified": False
}
print(profile["followers"])
#profile[0]
# KeyError: 0
# Predict: 5000, and profile[0] can't do anything because dictionaries aren't ordered by index
# Answer: because it's more meaningful & easier for dictionaries to be paired with a singular
# item rather than have to search through an entire index

#9
profile["followers"] += 50
profile["bio"] = "24, artist, activist, writer"
#print(profile)
#print(profile.get("age"))
# Predict: doesn't it print nothing? i know it doesn't necessarily count as an error
# Answer: it's safer because profile["age"] will specifically spit out an error message,
# whereas the .get command simply tells you that nothing can be found in the dictionary.

#10
print(f"{profile['username']} has {profile['followers']} followers and {len(feed)} posts. Top post: {feed[0]}")
# Predict: @snowlicorice has 5050 followers and 3 posts. Top post: i love anime
# Answer: list and dictionary