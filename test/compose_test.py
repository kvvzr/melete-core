# -*- coding: utf-8 -*-

import os, string, random

import sure
import melete.lyrics as Lyrics
import melete.rhythm as Rhythm
import melete.chord as Chord
import melete.melody as Melody

ts = Rhythm.TimeSignature(4, 2)
rhythms = [[0], [0, 96], [48, 96, 144], [0, 48, 96, 144]]
tree = Rhythm.RhythmTree(48, 1, ts, rhythms)

text = u'ぽよぽよぽよぽよぽよぽよぽよぽよ===あるう ひ もりのな か くまさん に であっ た あるう ひ もりのな か くまさん に であっ た'
lyrics = Lyrics.analyze(text)
lyrics = map(lambda l: Lyrics.divide(l['phoneme'], tree), lyrics)
beats = map(lambda l: Lyrics.pair(l, tree), lyrics)

c = Chord.Chord.from_name('C')
f = Chord.Chord.from_name('F')
f.inversion(1)
gsus4 = Chord.Chord.from_name('Gsus4')
gsus4.inversion(1)
prog = Chord.ChordProg(48, 4, [(c, 0), (f, 192), (gsus4, 384), (c, 576)])

note_range = Chord.note_range('C4', 'A5')

midi = Melody.create(ts, beats, prog, note_range)
savepath = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)]) + '.mid'

if not os.path.exists('log'):
    os.makedirs('log')

midi.save('log/' + savepath)
