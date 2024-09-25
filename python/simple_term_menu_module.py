from simple_term_menu import TerminalMenu

data = {
    'questions': 'Which phones do you like?',
    'answers' : ['Iphone 15 pro max', 'Samsung s20', 'Xiaomi 12 pro', 'Google pixel 6 pro', 'Huawei p40 pro', 'Iphone 13 pro max', 'Samsung s21', 'Xiaomi 12', 'Google pixel 6', 'Huawei p40']
}

choices = TerminalMenu(data['answers'], title=data['questions'])
select = choices.show()

print('Your choice: ', data['answers'][select])

if select == 0:
    print('Congrats! You answered correctly! ✅✅✅')
else:
    print('Oh no! You answered incorrectly! ❌❌❌')