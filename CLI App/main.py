# Day 9

while True:
    user_action = input("Enter add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    if "add" in user_action:
        todo = user_action[4:] + '\n'
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo.capitalize())
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        print("Todo Added.")

    elif "show" in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
            new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(new_todos):
                print(f"{index + 1}. {item}")

    elif "edit" in user_action:
        index = int(user_action[4:])
        index = index - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[index] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        print("List updated.")
    elif "complete" in user_action:
        index = int(user_action[9:])

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        print("Todo completed:", todos.pop(index - 1))

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif "exit" in user_action:
        break

print("Program closed.")
