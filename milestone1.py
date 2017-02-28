import runMelisma, sys, chordquality_identifier, convert_labels_to_roman_numerals


if len(sys.argv) != 3:
    print "usage: python milestone1.py <midifile> <desired key>"
    quit()

args = sys.argv
midifile = args[1]
desiredKey = args[2]

# chordsAndPitches, lowestNotesInChord = runMelisma.getChordsAndPitches('melisma2003/midifiles/kp/tchaik.symph6.mid')
chordsAndPitches, lowestNotesInChord = runMelisma.getChordsAndPitches(midifile)

chordsWithQuality = []

for i in range(len(chordsAndPitches)):
    chordsWithQuality.append(chordquality_identifier.chordquality_identifier(chordsAndPitches[i][0], chordsAndPitches[i][1]))

# romanNumerals = convert_labels_to_roman_numerals.label_to_rn(chordsWithQuality, lowestNotesInChord, 'C')
romanNumerals = convert_labels_to_roman_numerals.label_to_rn(chordsWithQuality, lowestNotesInChord, desiredKey)
print romanNumerals
