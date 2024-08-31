# Justice League 
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# members in the Justice League
print("Initial Justice League:")
print(justice_league)
print("Number of members:", len(justice_league))

#  Adding Batgirl and Nightwing as new members
justice_league.append(["Batgirl", "Nightwing"])
print("\nAfter adding Batgirl and Nightwing:")
print(justice_league)

# Wonder woman to beginning
justice_league.insert(0, justice_league.pop(justice_league.index("Wonder Woman")))
print("\nAfter making Wonder Woman the leader:")
print(justice_league)

# Moving Green Lantern 
justice_league.insert(justice_league.index("Flash"), justice_league.pop(justice_league.index("Green Lantern")))
print("\nAfter separating Aquaman and Flash:")
print(justice_league)

#Replace the existing list 
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\nNew Justice League:")
print(justice_league)

#sort alphabetically
justice_league.sort()
print("\nAfter sorting the Justice League alphabetically:")
print(justice_league)

#their
print("\nThe new leader is:", justice_league[0])