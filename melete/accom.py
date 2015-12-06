# -*- coding: utf-8 -*-
import mido

class AccomPattern:
    def __init__(self, pattern):
        self.pattern = pattern

def create_midi_track(rhythm, beat_num, chord_prog, pattern):
    accom = mido.MidiTrack()
    for t in range(beat_num):
        for i, s in enumerate(chord_prog.current(t).sounds):
            accom.append(mido.Message('note_on', note=s + 12 * 5, time=0))
        for i, s in enumerate(chord_prog.current(t).sounds):
            offset = 0
            if i == 0:
                offset = int(48 * 4 * rhythm.simple)
            accom.append(mido.Message('note_off', note=s + 12 * 5, time=offset))

    return accom
