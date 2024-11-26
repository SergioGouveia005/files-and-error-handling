def triangle_pattern(filename, length):
    content = ""
    for i in range (1, length + 2):
        content += "*" * (length + 2 - i) + "\n"
    with open(filename, "w") as file:
        file.write(content)

triangle_pattern("triangle_pattern.txt", 4)