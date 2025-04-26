def minMovesToSeat(seats, students):

    max_size = max(max(seats), max(students)) + 1
    arr_seats = [0] * max_size 
    arr_students = [0] * max_size

    for i in range(len(seats)):
        arr_seats[seats[i]] += 1

    for i in range(len(students)):
        arr_students[students[i]] += 1
    
    i = j = 0 

    moves = 0
    while (i < max_size) and (j < max_size):
        if arr_seats[i] > 0 and arr_students[j] > 0:
            moves += abs(i- j)
            arr_seats[i] -= 1
            arr_students[j] -= 1
        if arr_seats[i] == 0:
            i += 1
        if arr_students[j] == 0:
            j += 1
    
    return moves


print(minMovesToSeat([2,2,6,6], [1,3,2,6]))