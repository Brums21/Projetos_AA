import time

from filter_documents import get_and_filter_documents
from exact_counter import exact_counter as exact_counter_func

# algoritmo em slide #11 diapositivo 52 - the metwally et al. algorithm

def space_saving(text, k=5):
    start_time = time.time()
    
    counter = {}
    for char in text:
        if char in counter.keys():
            counter[char] += 1
        elif (len(counter.keys()) < k):
            counter[char] = 1
        else:
            dict_sort = sorted(counter.items(), key = lambda x: x[1], reverse=False)
            j = dict_sort[0]
            counter[char] = j[1] + 1;
            counter.pop(j[0])
            
    end_time = time.time()
            
    return counter, end_time-start_time
      
def incidency_stats_files_sc(file, counter_sc, exact_counter, k):
    
    exact_counter = dict(list(exact_counter.items())[:k])
    keys_exact = list(exact_counter.keys())
    keys_sc = list(counter_sc.keys())
    
    common_keys_order = sum(keys_exact[i] == keys_sc[i] for i in range(min(len(keys_exact), len(keys_sc)))) # only items with equal order are counted
    common_keys = len(set(keys_exact) & set(keys_sc))
    
    file.write("k:" + str(k) + "\n")
    file.write("percentage_correct_keys: " + str((common_keys_order/k)*100) + "%\n")        
    file.write("percentage_correct_order: " + str((common_keys/k)*100) + "%\n")     

      
def main():      
    text_en, text_es, text_fr = get_and_filter_documents()

    all_texts = [text_en, text_es, text_fr]
    files_languages = ["en", "es", "fr"]

    file_times = open("./results/time_space_saving.txt", "w")

    for a in range(len(all_texts)):
        text = all_texts[a]
        
        exact_counter, _ = exact_counter_func(text)
        
        file = open("./results/space_saving_" + files_languages[a] +".txt", "w")
        
        file_times.write(files_languages[a] + "\n")

        for n in [3, 5, 11]:
            counter, temp = space_saving(text, n)
            incidency_stats_files_sc(file, counter, exact_counter, n)
            file_times.write("n: " + str(n) + "\n" + str(temp) + "\n")
         
        file.close()
        
    file_times.close()

if "__main__"==__name__:
    main()