# -*- coding: utf-8 -*-

import os, string, random
import mido
import sure
import melete.accom as Accom
import melete.rhythm as Rhythm
import melete.chord as Chord

ts = Rhythm.TimeSignature(4, 2)

c = Chord.Chord.from_name('C')
f = Chord.Chord.from_name('F')
f.inversion(1)
gsus4 = Chord.Chord.from_name('Gsus4')
gsus4.inversion(1)
prog = Chord.ChordProg(48, 4, [(c, 0), (f, 192), (gsus4, 384), (c, 576)])

pattern = {
        0.125: {'length': 0.125, 'notes': [0]},
        0.25: {'length': 0.25, 'notes': [1, 2]},
        0.5: {'length': 0.25, 'notes': [2]},
        0.75: {'length': 0.25, 'notes': [0, 100]},
}

with mido.MidiFile(ticks_per_beat=48, charset='utf-8') as midi:
    track = Accom.create_midi_track(ts, 8, prog, pattern)
    midi.tracks.append(track)

savepath = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)]) + '.mid'

if not os.path.exists('log'):
    os.makedirs('log')

midi.save('log/' + savepath)
