import mingus.core.notes as notes
from mingus.containers import *
from mingus.midi import fluidsynth
import time

class ChordCharacter:
    def __init__(self, base, gender, voicing_name):
        self.base_ = base
        self.gender_ = gender
        self.voicing_name_ = voicing_name

class ChordTemplate:
    def __init__(self):
        self.notes_ = []
        self.characters_ = []

    def SetNotes(self, *strs):
        for str in strs:
            n = Note(str)
            self.notes_.append(n)

    def AddCharacter(self, character):
        self.characters_.append(character)

    def GetContainer(self):
        c = NoteContainer()
        for n in self.notes_:
            c += n
        return c

#c.SetNotes('D-3', 3, [0, 5, 10, 15, 19])
templates = []
c = ChordTemplate()
c.SetNotes('D-3', 'G-3', 'C-4', 'F-4', 'A-4')
c.AddCharacter(ChordCharacter('D', 'm7', 'SoWhat'))
templates.append(c)

c = ChordTemplate()
c.SetNotes('F-3', 'B-3', 'E-4', 'A-4', 'D-5')
c.AddCharacter(ChordCharacter('D', '69', 'Fourths'))
c.AddCharacter(ChordCharacter('D', '69', 'Fourths'))
templates.append(c)

#print(notes.is_valid_note("D#"))

#nc = NoteContainer(['C', 'E', 'G'])
# middle Aminor is A3, C4, E4
#a = Note('A-3')
#n.from_int(44)
#nc = NoteContainer()
#nc += a
nc1 = templates[0].GetContainer()
nc2 = templates[1].GetContainer()

#fluidsynth.init("AJH_Piano.sf2","coreaudio","foo.wav")
fluidsynth.init("SalC5Light2.sf2","coreaudio","foo.wav")
fluidsynth.play_NoteContainer(nc1)
fluidsynth.midi.sleep(.2)
fluidsynth.stop_NoteContainer(nc1)
fluidsynth.play_NoteContainer(nc2)
fluidsynth.midi.sleep(1)
fluidsynth.stop_NoteContainer(nc2)
