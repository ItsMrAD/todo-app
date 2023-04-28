while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.startswith("show"):

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item.title()}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter New Todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print('Your Command Is Not Valid')
            continue
    elif user_action.startswith("complete"):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        number = int(user_action[9:])

        index = number - 1
        todo_to_remove = todos[index].strip('\n')

        todos.pop(index)

        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)

        message = f"{todo_to_remove.title()} was removed from the list"
        print(message)
    elif user_action.startswith("exit"):
        break
    else:
        print('Command is not valid')

print('Bye')
