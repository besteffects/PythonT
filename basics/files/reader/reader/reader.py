# Program for compressing files to .bz2 and .gz
import os
from basics.files.reader.reader.compressed import bzipped,gzipped

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener,
}

class Reader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension, open())
        self.filename = filename
        self.f = open(self.filename)

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()

# to call:
# import reader
# r = reader.Reader('test.bz2')
# r.read()
# r = reader.Reader('test.gz2')
# r.read()
# r.close()
