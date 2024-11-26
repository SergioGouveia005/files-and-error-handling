import os
def write_to_file(filename, content):
    # complete the function
    with open(filename, "w") as file:
        file.write(content)


def read_from_file(filename):
    # complete the function
    with open(filename, "r") as file:
        content = file.read()
    return content

def append_to_file(filename, content):
    # complete the function
    with open(filename, "a") as file:
        file.write("\n" + content)

def remove_file(filename):
   # complete the function
    os.remove(filename)