computer_choice = 'rock'
user_choice = input("Enter rock, paper, or python:\n")
# Multiple if's means your code would go and check all the if conditions, where as in case of elif, if one if condition
# satisfies it would not check other conditions..
if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'python':
    print('WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
else:
    print('You lose :( Computer wins :D')
