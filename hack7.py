highscore = [45, 67, 56, 78]
for pos,item in enumerate(highscore):
    print(pos+1, end='')
    print('.',item)
newscore = int(input('Enter your new high score: '))
highscore.append(newscore)
print('Your new high scores are: ')
for pos,item in enumerate(highscore):
    print(pos+1, end='')
    print('.',item)