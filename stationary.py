class Pencil:
    def __init__(self, point_dur=10, length=5, eraser_dur=24):
        self.point_dur = point_dur
        self.default_point_dur = point_dur
        self.eraser_dur = eraser_dur
        self.length = length

    def _degradation_cost(self, c, is_write):
        """Returns the point/eraser degradation cost of writing/erasing a char C"""
        cost = 1
        if c == ' ' or c == '\n':
            cost = 0
        if is_write and c.isupper():
            cost = 2
        return cost

    def _write_char(self, c, cost):
        """Degrades the Pencil by COST for writing C and returns char to write"""
        to_write = ""
        if self.point_dur - cost >= 0:
            to_write += c
        elif self.length > 0:
            self.length -= 1
            self.point_dur += self.default_point_dur
            to_write += c
        self.point_dur -= cost
        return to_write

    def write(self, text, paper):
        """Writes a TEXT onto a PAPER"""
        if not isinstance(text, str):
            raise TypeError("Please provide a string argument")
        if not isinstance(paper, Paper):
            raise TypeError("Please provide a Paper object")

        writeable = ""
        for i in range(len(text)):
            c = text[i]
            cost = self._degradation_cost(c, True)
            writeable += self._write_char(c, cost)

        paper.text += writeable

    def erase(self, text, paper):
        """Erases a TEXT, if found, from a PAPER"""
        if not isinstance(text, str):
            raise TypeError("Please provide a string argument")
        if not isinstance(paper, Paper):
            raise TypeError("Please provide a Paper object")

        start = paper.text.rfind(text)

        if start > -1:
            erased = []
            for i in reversed(range(len(text))):
                c = text[i]
                cost = self._degradation_cost(c, False)
                if text[i] == ' ' or text[i] == '\n':
                    erased.append(text[i])
                elif self.eraser_dur > 0:
                    erased.append(' ')
                else:
                    erased.append(text[i])
                self.eraser_dur -= cost

            erased = ''.join(reversed(erased))
            end = start + len(text)
            paper.text = paper.text[:start] + erased + paper.text[end:]

    def edit(self, text, paper, start=0):
        """Writes TEXT over existing text on a PAPER, if possible"""
        if not isinstance(text, str):
            raise TypeError("Please provide a string argument")
        if not isinstance(paper, Paper):
            raise TypeError("Please provide a Paper object")
        if start >= len(paper.text):
            raise IndexError("Please provide a valid index to begin editing")

        end = min(start + len(text), len(paper.text))

        edited = ""
        for i in range(start, end):
            c = text[i - start]
            cost = self._degradation_cost(c, True)

            if paper.text[i] == c:
                edited += paper.text[i]
            elif self.point_dur - cost < 0 and self.length == 0:
                if cost < 2:
                    edited += paper.text[i]
                else:
                    cost = self._degradation_cost('@', True)
                    edited += self._write_char('@', cost)
            else:
                if paper.text[i] == ' ':
                    edited += self._write_char(c, cost)
                else:
                    cost = self._degradation_cost('@', True)
                    edited += self._write_char('@', cost)

        paper.text = paper.text[:start] + edited + paper.text[end:]


class Paper:
    def __init__(self, text=""):
        self.text = text
