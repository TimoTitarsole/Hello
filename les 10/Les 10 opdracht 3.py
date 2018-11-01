def code(invoerstring: str):
 print(''.join([chr(point) for point in [ord(character) + 3 for character in invoerstring]]))


code('RutteAlkmaarDen Helder')