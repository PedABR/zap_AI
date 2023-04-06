import sys

def remove_emojis(line):
    out = ""
    for char in line:
        if ord(char) <= 700:
            out += char
    return out
    

def each_line(stream):
    buffer = ''
    while True:
        chunk = stream.read(2048)
        if not chunk:
            yield buffer
            break
        buffer += chunk
        while True:
            try:
                part, buffer = buffer.split('\n', 1)
            except ValueError:
                break
            else:
                yield part

BASE_DIR = "../messages/all/"

file_name = sys.argv[1]
file_name = BASE_DIR + file_name

original = open(file_name+".txt", 'r')
copy = open(file_name+"_cleaned.txt", 'w')

for chunk in each_line(original):
    if "Arquivo de mídia oculto" not in chunk:
        copy.write(remove_emojis(chunk)+'\n')
    
original.close()
copy.close()