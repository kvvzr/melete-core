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

with mido.MidiFile(ticks_per_beat=48, charset='utf-8') as midi:
    track = Accom.create_midi_track(ts, 8, prog, [])
    midi.tracks.append(track)

savepath = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)]) + '.mid'

if not os.path.exists('log'):
    os.makedirs('log')

midi.save('log/' + savepath)
