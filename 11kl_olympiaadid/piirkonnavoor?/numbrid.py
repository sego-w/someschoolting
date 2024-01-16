def main():
    
    N = int(input())

    M = list(map(int, input().split()))

    sorted_M = sorted(M)
   
    missing_integers = []

    for i in range(1, N): 
        if sorted_M[i] - sorted_M[i - 1] > 1:
            missing_integers.extend(range(sorted_M[i - 1] + 1, sorted_M[i]))

    print(len(missing_integers))
    
    if len(missing_integers) > 0:
        print(' '.join(map(str, missing_integers)))

main()