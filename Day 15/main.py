import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It Is", now)
while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)
        # this means write_todos(filepath='todos.txt', todos_arg=todos)
    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item.title()}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter New Todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print('Your Command Is Not Valid')
            continue
    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()
            number = int(user_action[9:])

            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            functions.write_todos(todos)

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
