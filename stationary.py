class Pencil:
    def __init__(self, point_dur=10, length=5, eraser_dur=10):
        self.point_dur = point_dur
        self.default_point_dur = point_dur
        self.eraser_dur = eraser_dur
        self.length = length

    def write(self, text, paper):
        if not isinstance(text, str):
            raise TypeError('Please provide a string argument')

        writeable = ""
        for c in text:
            cost = 1
            if c == ' ' or c == '\n':
                cost = 0
            if c.isupper():
                cost = 2
            # print(c, cost, self.point_dur)
            if self.point_dur - cost >= 0:
                writeable += c
            elif self.length > 0:
                self.length -= 1
                self.point_dur += self.default_point_dur
                writeable += c
            self.point_dur -= cost

        paper.append(writeable)

    # def sharpen(self):


class Paper:
    def __init__(self):
        self.text = ""

    def append(self, new_text):
        self.text += new_text
