def manual_fill(A):
    for i in range(9):
        temp_list=[]
        for p in range(9):
            if i==p:
                temp_list.append(0)
            else:
                rep=int(input(f"Ingrese la cantidad de goles que el equipo {i} le acerto al equipo {p}"))
                temp_list.append(rep)
        A.append(temp_list)
    return A

def show_table(A):
    j=0
    print("    0 1 2 3")
    
    for i in range(len(A)):
        print(" ")
        print(f" {j}",end="  ")
        j=j+1
        for p in range(len(A[i])):
            print(A[i][p],end=" ")
    print(" ")