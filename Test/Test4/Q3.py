for i in range(1,22):
    for j in range(1,22):
        if( i == 1 or i == 21 or i + j == 22):
            print("*" , end = " ")
        else:
            print(" ", end= " ")
    print()