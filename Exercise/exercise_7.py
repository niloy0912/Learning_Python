files = ["a.txt", "b.txt", "c.txt"]

for content in files:
    file = open(f"Files/{content}", 'r')
    print(file.read())
