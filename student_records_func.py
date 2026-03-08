# Students records using Functions with parameters &  Arguments
def add_student():
    n = int(input("Enter no.of students:"))
    records = {}
    for i in range(1,n+1):
        name = input("Enter student number {i}:")
        marks = int(input("Enter student number {i} marks:"))
        records[name] = marks
    return records
def find_topper(records):
    max_marks = 0
    for name in records:
        if records[name] > max_marks:
            max_marks = records[name]
            Name = name
    print("Topper = ",Name, ':' , "Marks = ",max_marks)
def average(records):
    total = 0
    for marks in records.values():
        total = total + marks
    avg = total / len(records)
    return avg
def above_avg(records,avg):
    print("----Above average students----") 
    for name,marks in records.items():
        if marks > avg :
            print("Name : ",name , ':' , "Marks: " , ':',marks)
records = add_student()
find_topper(records)
avg = average(records)
print(f"Average Marks :{avg}")
above_avg(records,avg)
    
        