import string

def get_and_filter_documents(folder= "./files/"):
    
    stopword = "stopwords_"
    files = "odyssey_"
    
    extensions = ["en.txt", "es.txt", "fr.txt"]
    
    text_en = []
    text_es = []
    text_fr = []
    
    texts = [text_en, text_es, text_fr]

    for i in range(3):
        
        extension = extensions[i]
        
        with open(folder + stopword + extension, "r", encoding="utf-8", errors="replace") as stopword_file:
            stopwords = set(stopword_file.read().split())
        
        file = open(folder + files + extension, "r", encoding='utf-8', errors='replace')
        
        text = file.read()
    
        filtered_text = ' '.join(word for word in text.split() if word not in stopwords)
        text = ''.join(char.upper() for char in filtered_text if (char.lower() in string.ascii_lowercase or char.upper() in string.ascii_lowercase))

        texts[i] = text
        
        file.close()
    
    return texts[0], texts[1], texts[2]
    
    