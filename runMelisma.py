import os, time


def getChordsAndPitches(midifile):
    os.system('melisma2003/mftextNEW/mftext ' + midifile + ' > new.notes')
    time.sleep(1)
    os.system('melisma2003/meter/meter new.notes | melisma2003/harmony/harmony > output.txt')
    time.sleep(1)

    ignore = ['Beat', 'Finished', 'Chord', 'TPCNote', 'Analysis:']

    nums = [str(x) for x in range(1,10)]
    lastChord = None
    chordsAndPitches = []

    prevChord = None
    chordsStartAndEnd = []
    chordsStartAndEndDict = {}
    dictNotInitialized = True
    lowestNoteInChord = []

    with open('output.txt') as f:
        content = f.readlines()
        for row in content:
            chunks = row.split()
            chunksC = row.split()
            chunksN = row.split()

            if len(chunksC) > 0 and chunksC[0] == 'Chord':
                chunksC = chunksC[1:]

                if prevChord is None or chunksC[2] != prevChord:
                    chordsStartAndEnd.append((int(chunksC[0]),int(chunksC[1])))
                    prevChord = chunksC[2]
                else:
                    tup = chordsStartAndEnd[-1]
                    chordsStartAndEnd = chordsStartAndEnd[:len(chordsStartAndEnd)-1]
                    newTup = (tup[0], int(chunksC[1]))
                    chordsStartAndEnd.append(newTup)

            if len(chunksN) > 0 and chunksN[0] == 'TPCNote':

                if dictNotInitialized:
                    for t in chordsStartAndEnd:
                        chordsStartAndEndDict[t] = 99999
                    dictNotInitialized = False

                chunksN = chunksN[1:]

                for t in chordsStartAndEnd:
                    # if start time of note is at/after start of chord and end time of note is at/before end of chord
                    # then it was played during the segment of that chord
                    # check if it's the lowest midi value for that chord
                    if int(chunksN[0]) >= t[0] and int(chunksN[1]) <= t[1]:
                        if int(chunksN[2]) < chordsStartAndEndDict[t]:
                            chordsStartAndEndDict[t] = int(chunksN[2])

            if len(chunks) > 0 and chunks[0] not in ignore:
                # ----->>>>> added the dash to strip because of weird melisma output <<<<<----------
                chunks = [x.strip('>-x*<') for x in chunks]
                chunks = [x for x in chunks if (x != '<' and x != '+' and x != 'x' and x != '|' and x != '' and x not in nums)]
                chunks = chunks[1:]

                # now first item is chord label, all items after that are pitches from that segment
                if lastChord is None or chunks[0] != lastChord:
                    if len(chunks) > 1:
                        chordsAndPitches.append((chunks[0], chunks[1:]))
                    else:
                        chordsAndPitches.append((chunks[0], []))
                    lastChord = chunks[0]
                else:
                    if len(chunks) > 1:
                        tup = chordsAndPitches[-1]
                        chordsAndPitches = chordsAndPitches[:len(chordsAndPitches)-1]
                        newTup = (tup[0],tup[1] + chunks[1:])
                        chordsAndPitches.append(newTup)

    for t in chordsStartAndEnd:
        lowestNoteInChord.append(chordsStartAndEndDict[t])

    return chordsAndPitches, lowestNoteInChord
