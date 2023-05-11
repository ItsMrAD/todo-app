def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos)


while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos("todos.txt")

        todos.append(todo + '\n')

        write_todos('todos.txt', todos)
    elif user_action.startswith("show"):

        todos = get_todos("todos.txt")

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item.title()}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter New Todo: ")
            todos[number] = new_todo + '\n'

            write_todos('todos.txt', todos)
        except ValueError:
            print('Your Command Is Not Valid')
            continue
    elif user_action.startswith("complete"):
        try:
            todos = get_todos("todos.txt")
            number = int(user_action[9:])

            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            write_todos('todos.txt', todos)

            message = f"{todo_to_remove.title()} was removed from the list"
            print(message)
        except IndexError:
            print('There Is No Item With That Number')
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print('Command is not valid')

print('Bye')
