import runMelisma, os, pickle, csv

labels_to_solfege = {}
if os.path.isfile("labels_to_solfege.dat"):
    f = open("labels_to_solfege.dat", "r")
    u = pickle.Unpickler(f)
    labels_to_solfege = u.load()
    f.close()
else:
    with open("labels_to_solfege.csv", 'rb') as labelsToSolfegeCsv:
        csvReader = csv.reader(labelsToSolfegeCsv, delimiter=',')
        outputFile = open('labels_to_solfege.dat', 'wb')
        for row in csvReader:
            k = row[0]
            v = []
            for chroma in row[1:]:
                v.append(chroma)
            labels_to_solfege[k] = v
        p = pickle.Pickler(outputFile)
        p.dump(labels_to_solfege)
        outputFile.close()

print labels_to_solfege
chordsAndPitches, lowestNotesInChord = runMelisma.getChordsAndPitches('melisma2003/midifiles/kp/tchaik.symph6.mid')

for i in range(len(chordsAndPitches)):
    print chordsAndPitches[i], lowestNotesInChord[i]
