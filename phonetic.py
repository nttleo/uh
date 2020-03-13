# phonetic alphabet encoder (python)
from time import sleep
print('PHONETIC ALPHABET ENCODER!')
sleep(2)
print('what is the text that you want to encode?')
sleep(1)
while True:
    text = input('\n')
    print('wait a minute...')
    sleep(3)
    chars = list(text.lower())
    phonetic = {
    'a': 'alpha', 
    'b': 'bravo', 
    'c': 'charlie', 
    'd': 'delta', 
    'e': 'echo', 
    'f': 'foxtrot', 
    'g': 'golf', 
    'h': 'hotel', 
    'i': 'india', 
    'j': 'juliet', 
    'k': 'kilo', 
    'l': 'lima', 
    'n': 'november', 
    'm': 'mike', 
    'o': 'oscar', 
    'p': 'papa', 
    'q': 'quebec', 
    'r': 'romeo', 
    's': 'sierra', 
    't': 'tango', 
    'u': 'uniform', 
    'v': 'victor', 
    'w': 'whiskey', 
    'x': 'xray', 
    'y': 'yankee',
    'z': 'zulu'
    }
    print('your final result is: \n')
    def translate(code, chars):
        for chars in chars:
            if chars in code:
                    print(code[chars])
                    sleep(0.6)
            else:
                print(chars)
                sleep(0.3)
    translate(phonetic, chars)
    print('\nshow me another text.')
    continue