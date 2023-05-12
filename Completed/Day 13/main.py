def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of to-do items"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items list in hte text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# If you want to write multiline code \:
text_multiline1 = "Today I am learning python \
I am doing a course on Udemy\
I am on Day 13"
# Or use """
text_multiline2 = """Today I am learning python 
I am doing a course on Udemy
I am on Day 13"""

while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)
        # this means write_todos(filepath='todos.txt', todos_arg=todos)
    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item.title()}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter New Todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print('Your Command Is Not Valid')
            continue
    elif user_action.startswith("complete"):
        try:
            todos = get_todos()
            number = int(user_action[9:])

            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            write_todos(todos)

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
