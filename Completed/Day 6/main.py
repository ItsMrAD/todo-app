while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

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
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item.title()}"
                print(row)
        case "edit":
            number = int(input("Number Of The Todo To Edit: "))
            number = number - 1
            new_todo = input("Enter New Todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Number Of The Todo To Mark As Complete: ")) - 1
            todos.pop(number)
        case "exit":
            break
        case _:
            print("Invalid Command")
