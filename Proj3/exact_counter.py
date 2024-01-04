import time
import string 
import matplotlib.pyplot as plt

from filter_documents import get_and_filter_documents

def exact_counter(text):
    start_time = time.time()
    
    counter = {}
    for char in text:
        if char not in counter.keys():
            counter[char] = 0
        counter[char] += 1
    
    end_time = time.time()
    
    counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
    
    return counter, end_time-start_time

def plot_letter_hits(counter_en, counter_es, counter_fr):
    
    languages = ["English", "Spanish", "French"]
    
    letters = list(string.ascii_uppercase)
    
    plt.figure(figsize=(12, 6))
    for i in range(len(languages)):
        language = languages[i]
        counter = [counter_en, counter_es, counter_fr][i]
        hits = [counter.get(letter, 0) for letter in letters]
        plt.plot(letters, hits, marker="o", label=language, markersize=4)
    
    plt.xlabel('Letters')
    plt.ylabel('Hits')
    plt.title('Letter Hits in Different Languages')
    plt.legend()
    plt.savefig("./images/plot_letter_hits.png")
    plt.close()
    

def main():
    text_en, text_es, text_fr = get_and_filter_documents()

    counter_en, time_en = exact_counter(text_en)
    counter_es, time_es = exact_counter(text_es)
    counter_fr, time_fr = exact_counter(text_fr)

    file = open("./results/time_exact.txt", "w")

    file.write("en: " + str(time_en) +"\n")
    file.write("es: " + str(time_es) +"\n")
    file.write("fr: " + str(time_fr) +"\n")

    file.close()

    #create graph which shows which letters are more proeminent based on the counters
    plot_letter_hits(counter_en, counter_es, counter_fr)

if "__main__"==__name__:
    main()