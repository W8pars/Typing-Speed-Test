import time
import requests


website = 'https://random-word-api.herokuapp.com/word?number='

# ask user to begin test, else end testing
print('The test will begin after the first word starts.')
begin_test = input('Would you like to start test? y/n: ').lower()

while begin_test != 'n':
    if begin_test.startswith('y'):
        # ask how many words to test
        num_words = input('How many words would you like to test against? Enter a number: ')

        # send get request to get random json of words and save resulting json as list of words to test
        word_list = requests.get(website + num_words).json()
        print(f'Here is the full list of words:\n')
        print(word_list)
        # start clock
        test_start = time.time()

        for count,word in enumerate(word_list):
            word_to_test = ''
            while word_to_test != word_list[count]:
                print(word_list[count])
                word_to_test = input(':')
        test_end = time.time()
        average_speed = int(num_words) / (test_end - test_start)*60
        print(f'Your results are:\n{average_speed} words per minute')
        begin_test = input('Would you like to go again? y/n: ')
    elif begin_test.startswith('n'):
        print('Test ended. See you next time!')
        begin_test = 'n'

    else:
        print('Please enter a valid response to begin or end testing')