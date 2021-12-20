positions = open('positions.txt', 'r')
lines = positions.readlines()

horizontal_position = 0
depth = 0

for line in lines:
    value = int(''.join(filter(str.isdigit, line)))

    if "forward" in line:
        horizontal_position += value
    elif "down" in line:
        depth += value
    elif "up" in line:
        depth -= value

positions.close()

print("Horizontal Position: " + str(horizontal_position))
print("Depth: " + str(depth))
print("Horizontal Position * Depth = " + str(horizontal_position * depth))
input("Press any key to close")