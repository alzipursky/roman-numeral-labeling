import os, time

def getChordsAndPitches(midifile):
    os.system('melisma2003/mftextNEW/mftext ' + midifile + ' > new.notes')
    time.sleep(1)
    os.system('melisma2003/meter/meter new.notes | melisma2003/harmony/harmony > output.txt')
    time.sleep(1)

    ignore = ['Beat','Finished','Chord','TPCNote','Analysis:']

    nums = [str(x) for x in range(9)]
    lastChord = None
    chordsAndPitches = []

    with open('output.txt') as f:
        content = f.readlines()
        for row in content:
            chunks = row.split()
            if len(chunks) > 0 and chunks[0] not in ignore:
                chunks = [x.strip('>') for x in chunks]
                chunks = [x for x in chunks if (x != '<' and x != '+' and x != 'x' and x != '|' and x != '' and x not in nums)]
                chunks = chunks[1:]

                # now first item is chord label, all items after that are pitches from that segment
                if lastChord is None or chunks[0] != lastChord:
                    if len(chunks) > 1:
                        chordsAndPitches.append((chunks[0],chunks[1:]))
                    else:
                        chordsAndPitches.append((chunks[0],[]))
                    lastChord = chunks[0]
                else:
                    if len(chunks) > 1:
                        tup = chordsAndPitches[-1]
                        chordsAndPitches = chordsAndPitches[:len(chordsAndPitches)-1]
                        newTup = (tup[0],tup[1] + chunks[1:])
                        chordsAndPitches.append(newTup)
    return chordsAndPitches
