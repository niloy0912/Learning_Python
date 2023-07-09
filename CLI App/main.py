# Day 7

while True:
    user_action = input("Enter add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter todo: ") + '\n'
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case "show":
            file = open('todos.txt', 'r')
            todos = file.readlines()
            new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(new_todos):
                print(f"{index + 1}. {item}")
            file.close()
        case "edit":
            index = int(input("Enter the index of the todo: "))
            index = index - 1
            new_todo = input("Enter new todo: ")
            todos[index] = new_todo
            print("List updated.")
        case "complete":
            index = int(input("Enter the index of the todo to complete: "))
            print("Todo completed:", todos.pop(index - 1))
        case "exit":
            break

print("Program closed.")
