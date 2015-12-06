# -*- coding: utf-8 -*-
import mido

class AccomPattern:
    def __init__(self, pattern):
        self.pattern = pattern

def create_midi_track(rhythm, beat_num, chord_prog, pattern):
    accom = mido.MidiTrack()
    for t in range(beat_num):
        sounds = chord_prog.current(t).sounds
        prev = 0.0

        for j, at in enumerate(pattern.iterkeys()):
            for i, a in enumerate(pattern[at]['notes']):
                offset = 0
                if i == 0:
                    offset = int(48 * 4 * rhythm.simple * (at - prev))
                accom.append(mido.Message('note_on', note=sounds[a % len(sounds)] + 12 * 5, time=offset))

            for i, a in enumerate(pattern[at]['notes']):
                offset = 0
                if i == 0:
                    offset = int(48 * 4 * rhythm.simple * pattern[at]['length'])
                accom.append(mido.Message('note_off', note=sounds[a % len(sounds)] + 12 * 5, time=offset))

            prev = at + pattern[at]['length']

    return accom
