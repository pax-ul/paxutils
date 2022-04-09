from src.paxutils.path import Path

path = Path('narcity.csv', course='GIF-U016')
print(path, path.exists())

path /= 'toto'
print(path, type(path))

print('tata' / path)
