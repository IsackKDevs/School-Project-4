#Isack Kipanga
#12/02/2022


import datetime
import matplotlib.pyplot as plt
import numpy as np

def main():
    golferNames = []
    scores = []
    golferCount = 0
    
    def inputInfo(golferCount):
        
        Count = input('Are there any golfer cards to input? (y/n): ')
        while Count != 'n':
            score = int(input('Enter a golfer score: '))
            scores.append(score)
            names = input('Enter a golfer name: ')
            golferNames.append(names)
            golferCount += 1
            Count = input("Do you have more golfers to enter? (y/n): " )
            print()
            if Count == 'n':
                break
            

    inputInfo(golferCount)

    def displayAll(golferNames, scores, golferCount):

        curDate = datetime.datetime.now()
        
        print('     SPRINGFORK AMATEUR GOLD CLUB \n' ' TOURNAMENT DATE:', curDate)
        print(('GOLFER NAME'), format('SCORE', '>40s'))
        print('-'*30, format('-'*7, '>21.5s'))
        
        number_of_golfers = len(golferNames)

        total = 0
        for n in golferNames:
            print(n)
            
        for num in (scores):
            print(f"{num :>52d}")
            total += num
            average = total / len(scores)
            
        winner = min(golferNames)
        
        print()
        print('Average score for all golfers', f"{average :>21f}")
        print('Winner is',winner, 'with the score',min(scores), 'out of', number_of_golfers, 'golfers' )
        
    displayAll(golferNames, scores, golferCount)
    def matli(golferNames, scores):

        x = np.array(golferNames[0:])
        y = np.array(scores[0:])
        plt.bar(x,y, width = 0.5)
        plt.show()
  
    matli(golferNames, scores)


main()
