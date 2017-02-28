import runMelisma, sys, chordquality_identifier, convert_labels_to_roman_numerals

if len(sys.argv) != 2:
    print "usage: python milestone2.py <midifile> <desired key>"
    quit()

args = sys.argv
midifile = args[1]
keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

highest_score = 0
correct_key = ""
correct_romanNumerals = []
chordsAndPitches, lowestNotesInChord = runMelisma.getChordsAndPitches(midifile)

for i in range(12):

    chordsWithQuality = []

    for j in range(len(chordsAndPitches)):
        chordsWithQuality.append(
            chordquality_identifier.chordquality_identifier(chordsAndPitches[j][0], chordsAndPitches[j][1]))

    # romanNumerals = convert_labels_to_roman_numerals.label_to_rn(chordsWithQuality, lowestNotesInChord, 'C')
    romanNumerals = convert_labels_to_roman_numerals.label_to_rn(chordsWithQuality, lowestNotesInChord, keys[i])
    # print 'key: ' + keys[i] + ';Roman Numerals: ',
    # print romanNumerals

    # Scoring Is Calculated Here
    num_minor_tonic = 0
    num_major_tonic = 0
    score = 0
    for k in range(len(romanNumerals)):
        if romanNumerals[k] is None:
            continue
        if romanNumerals[k][0] == "I":
            score += 1
            num_major_tonic += 1

        if romanNumerals[k][0] == "i":
            score += 1
            num_minor_tonic += 1

        if romanNumerals[k][0] == "V" or romanNumerals[k][0] == "v":
            score += 1
        if romanNumerals[k][0:1] == "IV" or romanNumerals[k][0:1] == "iv":
            score += 1
        if romanNumerals[k][0:1] == "IV" or romanNumerals[k][0:1] == "iv":
            score += 1
        if k == (len(romanNumerals) - 1) and romanNumerals[k - 1] is not None:
            if (romanNumerals[k - 1][0] == "V" and romanNumerals[k][0] == "I") or \
                    (romanNumerals[k - 1][0] == "V" and romanNumerals[k][0] == "i"):
                score += 5
    if score > highest_score:
        highest_score = score
        correct_romanNumerals = romanNumerals
        correct_key = keys[i]
        if num_major_tonic > num_minor_tonic:
            correct_key += ' major'
        else:
            correct_key += ' minor'

print 'This excerpt is in the key of: ' + correct_key
print correct_romanNumerals
