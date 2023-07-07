todos = []

while True:
    user_action = input("Enter add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter todo: ")
            todos.append(todo.capitalize())
        case "show":
            for index, item in enumerate(todos):
                print(f"{index + 1} {item}")
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
