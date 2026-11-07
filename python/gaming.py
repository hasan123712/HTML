

import os

print("================================")
print("GAMING STATISTICS ORGANIZER")
print("================================")



minecraft_stats = [
    "Minecraft has different game modes\n",
    "Players can build houses and explore\n",
    "Diamonds are a valuable resource\n"
]

roblox_stats = [
    "Roblox has many different games\n",
    "Players can create their own games\n",
    "Roblox supports multiplayer gaming\n"
]

with open("minecraft-stats.txt", "w") as f:
    f.writelines(minecraft_stats)

with open("roblox-stats.txt", "w") as f:
    f.writelines(roblox_stats)

print("Sample gaming files created successfully.")




print("\nPART 1: Minecraft Statistics")

with open("minecraft-stats.txt", "r") as f:
    for line in f:
        print(line.strip())


print("\nPART 2: Word Count in Roblox Statistics")

with open("roblox-stats.txt", "r") as f:
    for line in f:
        words = line.split()
        print(len(words), "words ->", line.strip())




combined_file = "all-gaming-stats.txt"

print("\nPART 3: Checking Combined File")

if os.path.exists(combined_file):
    print(combined_file, "already exists.")
else:
    print(combined_file, "does not exist yet.")




print("\nPART 4: Remove Old File")

if os.path.exists(combined_file):
    os.remove(combined_file)
    print("Old combined file removed.")
else:
    print("No old combined file to remove.")



print("\nPART 5: Merging Files")

with open(combined_file, "w") as output:
    output.write("=== MINECRAFT STATISTICS ===\n")

    with open("minecraft-stats.txt", "r") as minecraft:
        output.write(minecraft.read())

    output.write("\n=== ROBLOX STATISTICS ===\n")

    with open("roblox-stats.txt", "r") as roblox:
        output.write(roblox.read())

print("Minecraft and Roblox statistics merged successfully.")




print("\nCombined Gaming Statistics:")

with open(combined_file, "r") as f:
    for line in f:
        print(line.strip())




print("\n================================")
print("GAMING STATISTICS SUMMARY")
print("================================")
print("with open() as f: Used for safe file handling.")
print("split(): Used to count words in each line.")
print("os.path.exists(): Used to check if a file exists.")
print("os.remove(): Used to delete an old file.")
print("File Merge: Minecraft and Roblox statistics combined into one file.")
print("================================")