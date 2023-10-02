import os

current_dir = os.path.dirname(__file__)
icons_paths = []

for file in os.listdir(current_dir):
    if file.endswith('.svg'):
        icons_paths.append(file)

with open('icons.qrc', 'w') as qrc_file:
    qrc_file.write('<!DOCTYPE RCC>\n<RCC version="1.0">\n<qresource>\n')

    for path in icons_paths:
        qrc_file.write(f'    <file>{path}</file>\n')

    qrc_file.write('</qresource>\n</RCC>')
    
    print("Resource file 'icons.qrc' has been generated.")