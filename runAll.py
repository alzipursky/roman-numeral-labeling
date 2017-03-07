import os


for filename in os.listdir('melisma2003/midifiles/kp'):
    if filename != 'README':
        print filename
        filename = 'melisma2003/midifiles/kp/' + filename
        os.system('python milestone2Tmp2.py ' + filename)
