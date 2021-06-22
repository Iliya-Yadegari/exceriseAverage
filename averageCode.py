exercise1 = input('Name of exercise 1: ')
score_exercise1 = int(input('Score received for exercise 1: '))
total_exercise1 = int(input('Total points possible for exercise 1: '))

exercise2 = input('Name of exercise 2: ')
score_exercise2 = int(input('Score received for exercise 2: '))
total_exercise2 = int(input('Total points possible for exercise 2: '))

exercise3 = input('Name of exercise 3: ')
score_exercise3 = int(input('Score received for exercise 3: '))
total_exercise3 = int(input('Total points possible for exercise 3: '))

total = score_exercise1 + score_exercise2 + score_exercise3

avg = total / 30

print('Exercise         Score       Total possible')
print(f'{exercise1}     {score_exercise1}    {total_exercise1}')
print(f'{exercise2}     {score_exercise2}    {total_exercise2}')
print(f'{exercise2}     {score_exercise2}    {total_exercise2}')
print(f'Total            {total}              30') 
print(f'Your total is {total} out of 30, or {avg}')