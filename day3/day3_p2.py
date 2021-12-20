binary_input = open('input.txt', 'r')
lines = binary_input.readlines()

i = 0
j = 0
occurences_for_0 = 0
occurences_for_1 = 0
final_gamma_binary_str = ''
final_epsilon_binary_str = ''

while i < 12:
    for line in lines:

        digit_cursor = int(line[j])
        
        if digit_cursor == 0:
            occurences_for_0 += 1

        if digit_cursor == 1:
            occurences_for_1 += 1

    result = {0: occurences_for_0, 1: occurences_for_1}

    gamma_winner = max(result, key=result.get)
    epsilon_winner = min(result, key=result.get)

    final_gamma_binary_str += str(gamma_winner)
    final_epsilon_binary_str += str(epsilon_winner)
    
    occurences_for_0 = 0
    occurences_for_1 = 0

    i += 1
    j += 1

binary_input.close()

gamma_rate = int(final_gamma_binary_str, 2)
epsilon_rate = int(final_epsilon_binary_str, 2)

print("The gamma rate is: " + str(gamma_rate))
print("The epsilon rate is: " + str(epsilon_rate))
input("gamma rate * epsilon rate = " + str(gamma_rate * epsilon_rate))
input("Press any key to close")
