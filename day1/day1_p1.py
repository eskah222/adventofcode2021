measurements = open('measurement.txt', 'r')
lines = measurements.readlines()

increasing_depth = 0
i = 0

for line in lines:
    
    if i == 0:
        increasing_depth += 1
        pass

    else:
        
        if lines[i] > lines[i-1]:
            increasing_depth += 1

    i += 1

measurements.close()

print("The number of increasing depth measurements is: " + str(increasing_depth))
input("Press any key to close")


