lines = ["Arjun 90\n","Krishna 95\n","Mahesh 80\n","Bob 35"]
with open("result.txt","w") as f:
    f.writelines(lines)
with open("result.txt","r") as f:
    lines = f.readlines()
result_lines = []
for line in lines:
    parts = line.strip().split()
    name = parts[0]
    marks = int(parts[1])
    if marks >=50 :
        status = "student Pass"
    else :
        status = "Student Fail"
    new_line = f"{name.upper()} {marks} {status}\n"
    result_lines.append(new_line)
with open("Result.txt","w") as f:
    f.writelines(result_lines)