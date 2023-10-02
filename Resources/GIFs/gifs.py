import os

current_dir = os.path.dirname(__file__)
gifs_paths = []

for file in os.listdir(current_dir):
    if file.endswith('.gif'):
        gifs_paths.append(file)

with open('gifs.qrc', 'w') as qrc_file:
    qrc_file.write('<!DOCTYPE RCC>\n<RCC version="1.0">\n<qresource>\n')
    
    for path in gifs_paths:
        qrc_file.write(f'    <file>{path}</file>\n')
    
    qrc_file.write('</qresource>\n</RCC>')
    
    print("Resource file 'gifs.qrc' has been generated.")