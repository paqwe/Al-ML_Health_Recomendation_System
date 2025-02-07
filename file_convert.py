import json
import csv

with open ("response_1.json","r") as f:
    data = json.load(f)
    health_problems=data["health_problems"]


with open ("response_1.csv","w") as f:
    fieldnames = health_problems.keys()
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    for i in health_problems:
        writer.writerow(i)



