import sys

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
copy = open(file_name+"_notime.txt", 'w')

for chunk in each_line(original):
    copy.write(chunk[19:]+"\n")
    
original.close()
copy.close()
