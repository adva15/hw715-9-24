# start

Good_results = 0
the_highest_score = 0
world_record = 6.23
new_record = world_record

name:str=str(input("name Olympics"))
result: float = float(input("High jump results of 7 countries in the Olympics:"))

for i in range(7):
    if result < 5.80:
        print("none")
        continue

else:
    if result <= 5.80:
        Good_results+=1
        new_record =+1
        the_highest_score+=1
        print(f"Good_results{Good_results}"f"new_record{new_record},"f"new_record{name}")


Good_results: float = the_highest_score/world_record
print(f"the_highest_score{the_highest_score}, average = {new_record:.2f},"f"new_record{name}")

