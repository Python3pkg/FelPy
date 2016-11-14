class rnr():
    def do(question):
        while True:
            answer = input(question.capitalize() + ': ')
            confirm = input('Is your ' + question + ' ' + answer + '? (y/n) ')
            if confirm == 'y':
                return answer
                break
            elif confirm == 'n':
                print ('Try again')
            else:
                print ('I didn\'t understand you')
