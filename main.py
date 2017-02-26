import runMelisma, os, pickle, csv, chordquality_identifier, convert_labels_to_roman_numerals, inversion_calculator, notes_to_chroma

chordsAndPitches, lowestNotesInChord = runMelisma.getChordsAndPitches('melisma2003/midifiles/kp/tchaik.symph6.mid')

chordsWithQuality = []

for i in range(len(chordsAndPitches)):
    chordsWithQuality.append(chordquality_identifier.chordquality_identifier(chordsAndPitches[i][0],chordsAndPitches[i][1]))

romanNumerals = convert_labels_to_roman_numerals.label_to_rn(chordsWithQuality,lowestNotesInChord,'D')
print romanNumerals
