def copy_contents(source_file, destination_file):
    try:
        with open(source_file, "r") as file:
            contents = file.read()
        with open(destination_file, "w") as file:
            file.write(contents)
    except FileNotFoundError:
        print("source_file does not exist")

copy_contents("temp1.txt", "temp2.txt")