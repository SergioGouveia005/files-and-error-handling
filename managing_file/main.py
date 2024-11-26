from managing_files import *

if __name__ == "__main__":
    try:
        # Create and Write to a file
        # Complete your code here...
        write_to_file("my_file.txt", "This is my first file")

        # Append to the file
        # Complete your code here...
        append_to_file("my_file.txt", "I have added another text")

        # Append to the file
        # Complete your code here...
        append_to_file("my_file.txt", "I am adding for the third time a text to see what will happen inside the file")

        #Read from the file
        # Complete your code here...
        print(read_from_file("my_file.txt"))
        

        #Read from the file
        # Complete your code here...

        print((read_from_file("my_file.txt").split("\n"))[0])
        

        # Write to the file
        # Complete your code here...
        write_to_file("my_file.txt", "This is my fourth text")


        #Read the updated content
        # Complete your code here...
        print(read_from_file("my_file.txt"))

        #Remove the file
        # Complete your code here...
        #remove_file("my_file.txt")
    except FileNotFoundError:
        print("File does not exist")