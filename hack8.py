highscore = [45, 67, 56, 78]
highscore.sort(reverse= True)
print("Your high scores are: ")
for pos,item in enumerate(highscore):
    print(pos+1, end='')
    print('.',item)
newscore = int(input('Enter your new high score: '))
highscore.append(newscore)
highscore.sort(reverse=True)
print('Your new high scores are: ')
for pos,item in enumerate(highscore):
    print(pos+1, end='')
    print('.',item)

print('Your 5 high scores are: ')
for i in range (5):
    print(i+1,end='')
    print('.',end=' ')
    print(highscore[i])
    

