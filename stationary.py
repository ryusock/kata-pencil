class Pencil:
    def __init__(self, point_dur=10, eraser_dur=10, length=2):
        self.point_dur = point_dur
        self.eraser_dur = eraser_dur
        self.length = length

    def write(self, text, paper):
        paper.append(text)

class Paper:
    def __init__(self):
        self.text = ""

    def append(self, new_text):
        self.text += new_text
