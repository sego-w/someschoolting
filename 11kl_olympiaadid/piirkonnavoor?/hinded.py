def main():
    def max_all(scr, sz):
        def sub_arr_sum(arr):
            max_so_far = max_ending_here = arr[0]
            for x in arr[1:]:
                max_ending_here = min(max_ending_here + x, x)
                max_so_far = min(max_so_far, max_ending_here)
            return max_so_far

        best = float('-inf')
        for left in range(sz):
            temp = [0] * sz
            for right in range(left, sz):
                for i in range(sz):
                    temp[i] += scr[i][right]
                best = max(best, -sub_arr_sum(temp))
                
        return best

    n = int(input())
    tbl = [list(map(lambda x: int(x) - 50, input().split())) for _ in range(n)]
    print(max_all(tbl, n))

main()