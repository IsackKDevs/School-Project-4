

def main():
    golferNames = []
    scores = []
    golferCounter = 0
    
    def inputInfo():
        golferCount = 1
        Count = 'y'
        while Count != 'n':
            score = int(input('Enter a golfer score: '))
            scores.append(score)
            names = input('Enter a golfer name: ')
            golferNames.append(names)

            golferCount += 1
            Count = input("Do you have more golfers to enter? (y/n): " )
            print()
            #if Count == 'n':
            #    print(golferNames, scores)
            sum_scires = sum(scores)
        while golferCounter <len(scores):
            sorter = scores.sort
            index = [0, sorter]
            print('The winner is ', index)
            break

    inputInfo()

main()

