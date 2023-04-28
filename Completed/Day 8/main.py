while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case "show":

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}-{item.title()}"
                print(row)
        case "edit":
            number = int(input("Number Of The Todo To Edit: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            number = number - 1
            new_todo = input("Enter New Todo: ")
            todos[number] = new_todo

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case "complete":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            number = int(input("Number Of The Todo To Mark As Complete: "))

            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

            message = f"{todo_to_remove.title()} was removed from the list"
            print(message)
        case "exit":
            break
        case _:
            print("Invalid Command")
