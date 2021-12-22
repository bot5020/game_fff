def one(mass, n , el):
    l, r, count = -1, n, 0
    while l + 1 < r:
        mid = (l + r) // 2
        #print(mid)
        if mass[mid] < el:
            l = mid
        elif mass[mid] > el:
            r = mid
        else:
            return el, count + 1
        count += 1
    else:
        return -1, count
el = int(input())
n = int(input())
m = [int(i) for i in input().split()]
print(one(m, n, el))
