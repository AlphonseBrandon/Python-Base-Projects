# Creating a dict that updates with user input

score_dict = {
    'Alphonse': 0,
    'Brandon': 0,
    'John': 0
}

def add_score(name, score):
    global score_dict
    score_dict[name] += score


while True:
        name = input('Enter name: ')
        if name == 'quit':
            break
        score = int(input('Enter score'))
        add_score(name, score)
        print(f'{name} \t {score_dict[name]}')

print(score_dict)