"""A module for dealing with BMP bitmap image files"""


def write_grayscale(filename, pixels):
    """Creates and writes a grayscale BMP file.
    Args:
      filename: The name of the BPM file to be created

      pixels: A rectangular image stored as a sequence of rows.
        Each row must be an iterable series of integers in the range 0-255.

    Raises:
          ValueError: If any of the integer values are out of range.
          OSError: If the file couldn't be written.
    """
    height = len(pixels)  # Counting the size of the image
    width = len(pixels[0])  # Number of items in 0th row to get the width, we assume that all rows have the same length

    with open(filename, 'wb') as bmp:  # open file using wb mode, encoding has no sense for binary files
        # BMP Header
        bmp.write(b'BM')  # b - bytes object

        size_bookmark = bmp.tell()  # The next four bytes hold the filesize as a 32-bit
        bmp.write(b'\x00\x00\x00\x00')  # little-endian integer. Zero placeholder for now. Four zero bytes using
        # \syntax to specify zeros

        bmp.write(b'\x00\x00')  # Unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00')  # Unused 16-bit integer - should be zero

        pixel_offset_bookmark = bmp.tell()  # The next four bytes hold the integer to the
        bmp.write(b'\x00\x00\x00\x00')  # pixel data. Zero placeholder for now

        #  Image Header
        bmp.write(b'\x28\x00\x00\x00')  # Image header size in Bytes
        bmp.write(_int32_to_bytes(width))  # Image width in pixels (converts int object into bytes object)
        bmp.write(_int32_to_bytes(height))  # Image height in pixels
        bmp.write(b'\x01\x00')  # Number of image planes
        bmp.write(b'\x08\x00')  # Bits per pixel 8 for grayscale
        bmp.write(b'\x00\x00\x00\x00')  # No compression
        bmp.write(b'\x00\x00\x00\x00')  # Zero for uncompressed images
        bmp.write(b'\x00\x00\x00\x00')  # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')  # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')  # Use whole color table
        bmp.write(b'\x00\x00\x00\x00')  # All colors are important

        # Color palette-a linear grayscale.Each pixel in an 8bit BMP image is an index into color table with 256 entries
        for c in range(256):
            bmp.write(bytes((c, c, c, 0)))  # Blue, Green, Red, Zero. Each entry is 4byte BGR color

        # Pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):  # BMP files are bottom to top (flip the order of the rows)
            row_data = bytes(row)
            bmp.write(row_data)
            #  Each pixel data in bmp file must be a multiple of 4 bytes long
            padding = b'\x00'*((4-(len(row) % 4)) % 4)  # Pad row to multiple of four bytes
            bmp.write(padding)

        # End of file (record the current position)
        eof_bookmark = bmp.tell()

        #  Fill in file size placeholder
        bmp.seek(size_bookmark)  # Seek for size bookmark we remembered on the beginning
        bmp.write(_int32_to_bytes(eof_bookmark))  # write the size stored in eof_bookmark

        # Fill in pixel offset placeholder (write 32bit)
        bmp.seek(pixel_offset_bookmark)


def _int32_to_bytes(i):
    """Convert an integer to four bytes in little-endian format."""
    # &: Bitwise-and
    # >>: Right-shift
    # The tuple is constructed which is then passed to the bytes constructor to produce a 4 bytes sequence
    return bytes((i & 0xff,
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff))


def dimensions(filename):
    """Determine the dimensions in pixels of a BMP image.

    Args:
        filename: The filename of a BMP file.

    Returns:
        A tuple containing two integers with the width
        and height in pixels.

    Raises:
        ValueError: If the file was not a BMP file.
        OSError: If there was a problem reading the file.
    """

    with open(filename, 'rb') as f:
        magic = f.read(2)
        if magic != b'BM':
            raise ValueError("{} is not a BMP file".format(filename))

        f.seek(18)
        width_bytes = f.read(4)
        height_bytes = f.read(4)

        return (_bytes_to_int32(width_bytes),
                _bytes_to_int32(height_bytes))


def _bytes_to_int32(b):
    """Convert a bytes object containing four bytes into an integer."""
    return b[0] | (b[1] << 8) | (b[2] << 16) | (b[3] << 24)
