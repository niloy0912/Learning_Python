# Day 8 - Do the exercise

while True:
    user_action = input("Enter add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter todo: ") + '\n'

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo.capitalize())

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                new_todos = [item.strip('\n') for item in todos]
                for index, item in enumerate(new_todos):
                    print(f"{index + 1}. {item}")

        case "edit":
            index = int(input("Enter the index of the todo: "))
            index = index - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[index] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            print("List updated.")
        case "complete":
            index = int(input("Enter the index of the todo to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            print("Todo completed:", todos.pop(index - 1))

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "exit":
            break

print("Program closed.")
