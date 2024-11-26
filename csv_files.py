import csv

def create_csv(filename, data):
    with open(filename, mode = "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(data)
        
def read_csv(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        #As a string
        rows = ""
        for row in reader:
            rows += str(row) + "\n"
        #As a list
        # rows = []
        # for row in reader:
        #     rows.append(row)
    return rows

def append_to_csv(filename, data):
    with open(filename, mode = "a", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(data)

content = [
    ['Name', 'Age', 'Grade'],
    ['Alice', 23, 'A'],
    ['Bob', 22, 'B'],
    ['Charlie', 24, 'A'],
    ['David', 22, 'C'],
    ['Eva', 23, 'B']
          ]

create_csv('students.csv', content)
print(read_csv("students.csv"))
append_to_csv('students.csv', ['Frank', 21, 'B'])
print()
read_csv("students.csv")

