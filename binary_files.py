#----Writing records using dump()----
import pickle
n = int(input("Enter number of studnets:"))
with open("records.dat","wb") as f:
    for i in range(1,n+1):
        s_id = int(input(f"Enter student-{i} id:"))
        s_name =input(f"Enter student-{i} name:")
        s_marks = int(input(f"Enter student-{i} marks:"))
        rec = {"id":s_id ,"name" : s_name ,"marks" : s_marks}
        pickle.dump(rec,f)
print("Student records written succesfully")
#----Reading records using load()----
import pickle
with open("records.dat","rb") as f:
    while True:
        try:
            r = pickle.load(f)
            print(r)
        except EOFError:
            break
f.close()
import pickle

FILE = "records.dat"

sid = int(input("Enter ID to update: "))
found = False
records = []
# Read all records
with open(FILE, "rb") as f:
    try:
        while True:
            rec = pickle.load(f)
            
            if rec["id"] == sid:
                print("Old Record:", rec)
                rec["marks"] = float(input("Enter new marks: "))
                found = True
            
            records.append(rec)
    except EOFError:
        pass
# Rewrite updated records
with open(FILE, "wb") as f:
    for rec in records:
        pickle.dump(rec, f)
# Output result
if found:
    print("Record updated successfully")
else:
    print("Record not found")