with open("test_data.txt","r") as fr:
    with open("dest_data.txt","w") as fw:
        for line in fr:
            fw.write(line)

print("Print the content of the file to new destination")

with open("dest_data.txt") as file:
    content = file.readlines()
    lines = len(content)
    words = sum([len(line.split()) for line in content])
    
    character = sum([len(line) for line in content])
print(f"line_count: {lines} , words_count: {words} and character_count: {character}")

import datetime

timestamp2 = datetime.datetime.now().isoformat()
timestamp1 = datetime.datetime.now()
print(timestamp1)
print(timestamp2)


