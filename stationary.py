class Pencil:
    def __init__(self, point_dur=10, length=5, eraser_dur=24):
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

        paper.text += writeable

    def erase(self, text, paper):
        if not isinstance(text, str):
            raise TypeError('Please provide a string argument')

        start = paper.text.rfind(text)
        if start > -1:
            erased = []
            for i in reversed(range(len(text))):
                cost = 1
                if text[i] == ' ' or text[i] == '\n':
                    cost = 0
                    erased.append(text[i])
                elif self.eraser_dur > 0:
                    erased.append(' ')
                else:
                    erased.append(text[i])
                self.eraser_dur -= cost
            erased = ''.join(reversed(erased))
            end = start + len(text)
            paper.text = paper.text[:start] + erased + paper.text[end:]


class Paper:
    def __init__(self):
        self.text = ""

    # def append(self, new_text):
    #     self.text += new_text
