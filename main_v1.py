
# from os import listdir
# from os.path import isfile, join
# onlyfiles = reversed([f for f in listdir(BASE_DIR) if isfile(join(BASE_DIR, f))])

# for item in onlyfiles:
#     with open(join(BASE_DIR, item), 'r') as content_file:
#         content = content_file.read()
#     print("Generating document for " + item + " ...")
#     completion = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {
#                 "role": "user",
#                 "content": "Write a documentation for following code: " + content
#             }
#         ]
#     )
#     print("Writing documentation into " + item + ".md")
#     with open(join(DOCS_DIR, item + ".md"), "w") as file:
#         file.write(completion.choices[0].message.content)
