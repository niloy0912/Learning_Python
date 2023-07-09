# translation: for each item in filenames take the item and add .txt
# start reading from the for loop part to understand the line
# this is called list comprehension

filenames = ["doc1", "doc2", "doc3"]

new_filenames = [item + ".txt" for item in filenames]

print(new_filenames)