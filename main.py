import matplotlib.pyplot as plt
import random

tests = 100
adas_crashes = 0
human_crashes = 0

for i in range(tests):

    ego_speed = random.randint(15,35)
    front_speed = random.randint(0,25)
    distance_between = random.randint(20,60)

    reaction_time = 1.5
    adas_reaction = 0.3

    human_distance = ego_speed * reaction_time
    adas_distance = ego_speed * adas_reaction
    front_distance = front_speed * reaction_time

    gap_human = distance_between - (human_distance - front_distance)
    gap_adas = distance_between - (adas_distance - front_distance)

    if gap_human <= 0:
        human_crashes +=1

    if gap_adas <=0:
        adas_crashes +=1


print("Human crashes:", human_crashes)
print("ADAS crashes:", adas_crashes)

#Plot Results
labels = ["Human","ADAS"]
values = [human_crashes, adas_crashes]

plt.bar(labels, values)
plt.title("Crash Comparison")
plt.ylabel("Number of crashes")
plt.show()
