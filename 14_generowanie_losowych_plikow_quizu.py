#! python3

import random

## Nazwy stanów (Klucze) oraz odpowiadające im stolice (wartości)
capitals={'Alabama' : 'Montgomery', 'Alaska' : 'Juneau', 'Arizona' : 'Phoenix', 'Arkansas' : 'Little rock', 'Kalifornia' : 'Sacramento', 'Kolorado' : 'Denver', 'Connecticut' : 'Hartford',
          'Delaver' : 'Dover', 'Floryda' : 'Tallahassee', 'Georgia' : 'Atlanta', 'Hawaje' : 'Honolulu', 'Idaho' : 'Boise', 'Illinois' : 'Springfield', 'Indiana' : 'Indianapolis',
          'Iowa' : 'Des Moines', 'Kansas' : 'Topeka', 'Kentucky' : 'Frankford', 'Luizjana' : 'Baton Rouge', 'Maine' : 'Augusta', 'Maryland' : 'Annapolis', 'Massachusetts' : 'Boston',
          'Michigan' : 'Lansing', 'Minesota' : 'Saint Paula', 'Mississippi' : 'Jackson', 'Missouri' : 'Jefferson City', 'Montana' : 'Helena', 'Nebrasca' : 'Lincoln', 'Nevada' : 'Carson City',
          'New Hampshire' : 'Concord', 'New Jersey' : 'Trenton', 'Nowy Meksyk' : 'Santa Fe', 'New York' : 'Albany', 'Karolina Północna' : 'Releigh', 'Dakota północna': 'Bismark',
          'Ohio' : 'Columbus', 'Oclahoma' : 'Oclahoma City', 'Oregon' : 'Salem', 'Pensylwania' : 'Harrisburg', 'Rhode Island' : 'Providence', 'Karolina Północna' : 'Columbia',
          'Dakota Północna' : 'Pierre', 'Tenessee' : 'Nashville', 'Teksas' : 'Austin', 'Utah' : 'Salt Lake City', 'Vermont' : 'Montpelier', 'Wirginia' : 'Richmond', 'Waszyngton' : 'Olympia',
          'Wirginia Zachodnia' : 'Charleston', 'Wisconsin' : 'Madison', 'Wyoming' : 'Cheyenne'}

## Wygenerowanie 35 plików quizu
for quizNum in range(10):
    #Utworzenie plików z quizem oraz odp
    quizFile = open('D:\\Python\\jak_kosic_trawe_pythonem\\quizy\\capitalsQuiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('D:\\Python\\jak_kosic_trawe_pythonem\\quizy\\capitalsQuiz_answers%s.txt' % (quizNum + 1), 'w')

    ##Zapis Nagłówka quizu
    quizFile.write('Imię i Nazwisko:\n\nData:\n\nGrupa:\n\n')
    quizFile.write((' ' * 20) + 'Quiz ze stolic stanów nr %s' % (quizNum + 1))
    quizFile.write('\n\n')

    ##Losowe ustalenie kolejności stanów
    states = list(capitals.keys())
    random.shuffle(states)

    ##Iteracja przez 50 stanów i utworzenie pytania dotyczącego każdego z nich
    for questionNum in range(50):
        ##Przygotowanie prawidłowych i błędnych odp
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        ##Zapis pytania i odpowiedzi w pliku quizu
        quizFile.write('%s. Co jest stolicą stanu %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('   %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        ##Zapis odpowiedzi w pliku
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
        quizFile.close()
        answerKeyFile.close()