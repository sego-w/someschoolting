def main():
    vaipmap = open("/Users/gustavtamkivi/Documents/Code/someschoolting/11kl_olympiaadid/vaibad.txt","r+").read()
    lists = vaipmap.split("\n")
    v = []
    q = []
    x = 0 
    for i in range(int(lists[0][0])+1):
        q.append((lists[i].split()))
    
    for e in range(len(q)-1):
        width = int(q[0][1]) - int(q[e][2]) - int(q[e][-1])
        height = int(q[0][2]) - int(q[e][0]) - int(q[e][1])
        area = width * height
        v.append(area)
    for number in v:
        x += int(number)
    print(f"Vaipade kogu pindala on {x} yhikut!")
    
    
    
# if __name__ == "__main__":
main()

