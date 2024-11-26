def triangle_pattern(filename, length):
    content = ""
    for i in range (length):
        content += "*" * (length - i) + "\n"
    with open(filename, "w") as file:
        file.write(content)

triangle_pattern("triangle_pattern.txt", 4)