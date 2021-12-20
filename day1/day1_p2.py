measurements = open('measurement.txt', 'r')
lines = measurements.readlines()

measurement_array = []

for line in lines:
    measurement_array.append(int(line))

measurements.close()

i = 0
increasing_depth = 1
triplet_sum_array = []

for value in measurement_array:

    if i == len(measurement_array)-3:
        break

    triplet_sum = measurement_array[i] + measurement_array[i+1] + measurement_array[i+2]
    triplet_sum_array.append(triplet_sum)
    
    if i > 0:
        if triplet_sum_array[i] > triplet_sum_array[i-1]:
            increasing_depth += 1
    
    i += 1

print("The number of increasing depth measurements is: " + str(increasing_depth))
input("Press any key to close")

