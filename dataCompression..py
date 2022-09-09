import zlib
import binascii
import bz2
"""
data = 'Hello world'
data = bytes(data, 'utf-8')

compressed_data = zlib.compress(data, 2)

print('Original data: ' +  data)
print('Compressed data: ' + binascii.hexlify(compressed_data))
"""

s = b'This is GFG author, and final year student.'
s = bz2.compress(s)
print(s)

# using bz2.decompress(s) method
t = bz2.decompress(s)
print(t)
