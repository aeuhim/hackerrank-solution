# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input().rstrip())
phonebook = dict()
for itr in range(size):
    name, phonenumber = input().rstrip().split(" ")
    phonebook[name] = phonenumber
while(True):
    try:
        entry = input().rstrip()
    except:
        break
    if entry not in phonebook:
        print("Not found")
        continue
    print(f'%s=%s' % (entry, phonebook[entry]))