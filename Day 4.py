s=INPUT.split('\n\n')

calls=list(map(int,s[0].split(',')))
boards=[i.split('\n') for i in s[1:]]
for i in range(len(boards)):
    boards[i]=[list(map(int,i.split())) for i in boards[i]]

def good(board,call,last):
    for i in board:
        if all(j in call for j in i):
            return(sum(k for l in board for k in l if k not in call)*last)
    for i in zip(*board):
        if all(j in call for j in i):
            return(sum(k for l in board for k in l if k not in call)*last)
    return -1

for i in range(len(calls)):
    for board in boards:
        if good(board,calls[:i+1],calls[i])!=-1:
            print(good(board,calls[:i+1],calls[i]))
            break
    else:
        continue
    break
print('-')
for i in range(len(calls)):
    rem=[]
    for board in boards:
        if good(board,calls[:i+1],calls[i])!=-1:
            print(good(board,calls[:i+1],calls[i]))
            rem.append(board)
    for j in rem:
        boards.remove(j)
