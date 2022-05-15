contentlines = ["Hello Everyone", "This Sunday, I am learning how can we convert txt files into pdf version and send it to the mail. Seems interesting,I know."]
with open ("readfile.txt","w") as f:
    f.write("\n".join(contentlines))
