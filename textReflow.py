def reflow(string):
    maxDist = 40
    newText = ""
    
    paragraphs = string.split("\n\n")
    for paragraph in paragraphs:
        paragraph = paragraph.replace("\n", " ")
        words = paragraph.split(" ")
        index = -1
            
        while paragraph != "":
            lineLength = 0
            line = ""
            while lineLength <= 40 and index < len(words):
                if index == len(words)-1:
                    line += words[index]
                    break
                if lineLength != 0:
                    line += words[index]
                    lineLength += 1
                    line += " "
                index += 1
                lineLength += len(words[index])
            index -= 1
            newText += line + "\n"
            paragraph = paragraph[len(line):]
        newText += "\n"
    return newText.strip()
