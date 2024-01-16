def main(): 

    def shortest_path(seq):
        remainder = len(seq) % 4
        if remainder != 0:
            t_needed = 4 - remainder
            t_seq = seq[-1] * t_needed
        else:
            t_needed = 0
            t_seq = ''

        print(t_needed)
        print(t_seq)

    n = int(input())
    s = input()
    shortest_path(s)

main()