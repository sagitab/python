from datetime import datetime
file_path = 'journal.txt'
text=""
i=0
while text!="done":
    timestamp = datetime.now().timestamp()
    dt_object = datetime.fromtimestamp(timestamp)
    dateFull=dt_object.strftime("%d-%m-%Y %H:%M:%S")
    text=input("enter text-")
    try:
     with open(file_path, 'x') as f:
         f.write(f'[{dateFull}] {text}')
    except FileExistsError:
     with open(file_path, 'a') as f:
        f.write(f'\n[{dateFull}] {text}')
    f = open(file_path, "r")
    print(f.read())
    i+=1
print(f"interation- {i}")
with open(file_path, 'r') as file:
        content = file.read()  # Read the entire content of the file
        words = content.split()  # Split content into a list of words
        word_count = len(words)  # Count the number of words
        print(f"Total number of words in '{file_path}': {word_count}")


    

