contents = ["All carrots something", "Something else", "Third content"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

# zip function basically creates tuples like the enumerate function but takes in two lists instead
for content, filename in zip(contents, filenames):
    file = open(f"Files/{filename}", 'w')
    file.write(content)
    file.close()
