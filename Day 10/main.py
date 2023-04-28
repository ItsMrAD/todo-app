while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:] + '\n'

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'show' in user_action:

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item.title()}"
            print(row)
    elif 'edit' in user_action:
        number = int(user_action[5:])

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        number = number - 1

        new_todo = input("Enter New Todo: ")
        todos[number] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'complete' in user_action:
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
    elif 'exit' in user_action:
        break
    else:
        print('Command is not valid')

print('Bye')
