filename = input("Enter today's date: ")

mood = (input("Enter mood: "))

content = input("Let your thoughts flow: ")

with open(f"Files/{filename}.txt", 'w') as file:
    file.write(mood + '\n')
    file.write(content)
