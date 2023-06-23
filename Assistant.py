#Install pywhatkit, datetime, wikipedia and pyjokes by pip first in your virtual environment.
import pywhatkit
import datetime
import wikipedia
import pyjokes




print("Welcome to Shosta Einstein Engine")
print("I can tell you jokes. Play your favourite music. Tell you the time. Give you a one line information about anything.")
print("Instructions:")
print("1. To play your music: '. + <music name>'")
print("2. To know the time just type: 'Time'")
print("3. To hear a joke just type: 'Joke'")
print("4. To know a one line information about anything type: 'What is + <name>")
var1 = input("What do you want? : ")

if '.' in var1:
    song = var1.replace('', '')
    print('Playing ' + song)
    pywhatkit.playonyt(song)
elif 'Time' in var1:
    time = datetime.datetime.now().strftime('%I:%M %p')
    print('Current time is ' + time)
elif 'What is ' in var1:
    person = var1.replace('Who is ', '')
    info = wikipedia.summary(person, 1)
    print(info)
elif 'Joke' in var1:
    print(pyjokes.get_joke())
else:
    print('Something went wrong. Please check the capitalization and type the command again.')
