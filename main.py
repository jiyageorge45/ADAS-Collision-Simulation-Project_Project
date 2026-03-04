#print("Hello ADAS")
#speed = 20        # meters per second
#acceleration = -6 # braking
#time = 3          # seconds

#distance = speed*time + 0.5*acceleration*time**2

#print("Car traveled:", distance, "meters")
'''
ego_speed = 25
front_speed = 10
distance_between = 40

reaction_time = 1.5

distance_ego = ego_speed * reaction_time
distance_front = front_speed * reaction_time

new_gap = distance_between - (distance_ego - distance_front)

print("Gap after reaction:", new_gap)
if new_gap <= 0:
    print("CRASH")
else:
    print("SAFE") 

Add ADAS Logic (Emergency Braking)
Now we add a smart system that brakes faster than human.

ego_speed = 25
front_speed = 10
distance_between = 40

reaction_time = 1.5
adas_reaction = 0.3

brake_deceleration = -8

human_distance = ego_speed * reaction_time
adas_distance = ego_speed * adas_reaction

front_distance = front_speed * reaction_time

gap_human = distance_between - (human_distance - front_distance)
gap_adas = distance_between - (adas_distance - front_distance)

print("Human gap:", gap_human)
print("ADAS gap:", gap_adas)

if gap_human <= 0:
    print("Human crashes")
else:
    print("Human safe")

if gap_adas <= 0:
    print("ADAS crashes")
else:
    print("ADAS safe")

'''
# Make It Real Research Level (Loop Many Tests)
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

#Plot Results (Make It Look Professional)
labels = ["Human","ADAS"]
values = [human_crashes, adas_crashes]

plt.bar(labels, values)
plt.title("Crash Comparison")
plt.ylabel("Number of crashes")
plt.show()
