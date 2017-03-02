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

# for i in chordsAndPitches:
#     print i

for i in range(len(keys)):

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
            if len(romanNumerals[k]) > 1:
                if romanNumerals[k][1] != "I" and romanNumerals[k][1] != "V":
                    score += 1
                    num_major_tonic += 1
            else:
                score += 1
                num_major_tonic += 1

        if romanNumerals[k][0] == "i":
            if len(romanNumerals[k]) > 1:
                if romanNumerals[k][1] != "i" and romanNumerals[k][1] != "v":
                    score += 1
                    num_major_tonic += 1
            else:
                score += 1
                num_major_tonic += 1

        if romanNumerals[k][0] == "V" or romanNumerals[k][0] == "v":
            if len(romanNumerals[k]) > 1:
                if romanNumerals[k][1] != "i" and romanNumerals[k][1] != "I":
                    score += 1
            else:
                score += 1
        if romanNumerals[k][0:2] == "IV" or romanNumerals[k][0:2] == "iv":
            score += 1
        if romanNumerals[k][0:2] == "VI" or romanNumerals[k][0:2] == "vi":
            if len(romanNumerals[k]) > 2:
                if romanNumerals[k][2] != "i" and romanNumerals[k][2] != "I":
                    score += 1
            else:
                score += 1
        if k >= 0 and romanNumerals[k - 1] is not None and romanNumerals[k] is not None:
            if romanNumerals[k - 1][0] == "V" and romanNumerals[k][0] == "I":
                actuallyV = False
                if len(romanNumerals[k-1]) > 1:
                    if romanNumerals[k-1][1] != "I":
                        actuallyV = True
                else:
                    actuallyV = True
                actuallyI = False
                if len(romanNumerals[k]) > 1:
                    if romanNumerals[k][1] != "I" and romanNumerals[k][1] != "V":
                        actuallyI = True
                else:
                    actuallyI = True
                if actuallyV and actuallyI:
                    score += 5
            elif romanNumerals[k - 1][0] == "V" and romanNumerals[k][0] == "i":
                actuallyV = False
                if len(romanNumerals[k-1]) > 1:
                    if romanNumerals[k-1][1] != "I":
                        actuallyV = True
                else:
                    actuallyV = True
                actuallyI = False
                if len(romanNumerals[k]) > 1:
                    if romanNumerals[k][1] != "i" and romanNumerals[k][1] != "v":
                        actuallyI = True
                else:
                    actuallyI = True
                if actuallyV and actuallyI:
                    score += 5
    print keys[i], score, romanNumerals
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
