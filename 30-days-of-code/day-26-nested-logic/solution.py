# Enter your code here. Read input from STDIN. Print output to STDOUT
d1, m1, y1 = map(int, input().split(' '))
d2, m2, y2 = map(int, input().split(' '))

if y1 < y2:
    print(0)
    quit()

if not (y1 == y2):
    print(10000)
    quit()

if not (m1 <= m2):
    print(500 * (m1 - m2))
    quit()

if not (d1 <= d2):
    print(15 * (d1 - d2))
    quit()

print(0)
