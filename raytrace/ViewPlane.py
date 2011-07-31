from . import Ray

class ViewPlaneRow(object):
    def __init__(self, row, maxcols):
        self._row = row
        self._maxcols = maxcols
    def __iter__(self):
        for column in xrange(self._maxcols):
            yield (column, self._row)
    def current_row(self):
        return self._row

class ViewPlane(object):
    def __init__(self, resolution, pixel_size):
        self.resolution = resolution
        self.pixel_size = pixel_size

    def __iter__(self):
        for row in xrange(self.resolution[1]):
            yield ViewPlaneRow(row, self.resolution[0])

