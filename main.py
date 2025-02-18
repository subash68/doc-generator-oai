from openai import OpenAI
client = OpenAI()

BASE_DIR = "src"
DOCS_DIR = "docs"

from os import listdir, walk, makedirs
from os.path import isfile, join, exists
for currentpath, folders, files in walk(BASE_DIR):
    for file in files:
        with open(join(currentpath, file), 'r') as content_file:
            content = content_file.read()
        print("Generating document for " + file + " ...")

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": "Write a documentation for following code: " + content
                }
            ]
        )
    
        print("Writing documentation into " + file + ".md")
        doc_path = DOCS_DIR + "/" + currentpath 
        if not exists(doc_path):
            makedirs(doc_path)
        with open(join(doc_path, file + ".md"), "w") as file:
            file.write(completion.choices[0].message.content)
