contents = ["Youtube is the most used social media",
            "Udemy is currently the biggest online learning platform",
            "Netflix is the biggest OTT provider"]
filenames = ["social.txt", "education.txt", "entertainment.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)