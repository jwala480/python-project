salaries =["John 20000\n","Priya 35000"]
with open("bonus.txt","w") as f:
     f.writelines(salaries)
with open("bonus.txt","r") as f:
    lines = f.readlines()
    result_lines =[]
    for line in lines:
        parts = line.strip().split()
        name = parts[0]
        salary = int(parts[1])
        total_amount = 0
        if salary < 30000:
            bonus_amount = salary*0.01
            total_amount = salary+bonus_amount
        else :
            bonus_amount = salary*0.05
            total_amount = salary+bonus_amount
        new_line = f"{name.upper()} {total_amount}\n"
        result_lines.append(new_line)
with open("bonus.txt","w") as f:
    f.writelines(result_lines)