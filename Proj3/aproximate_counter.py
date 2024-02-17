import os
import random
import time as tm

from utils import mean as calc_mean, \
                dev as calc_dev, \
                mad as calc_mad, \
                std_dev as calc_std_dev, \
                write_to_files_stats as file_write_stats, \
                sum_lists_with_same_order as compare_lists
from exact_counter import exact_counter as exact_counter_func
from filter_documents import get_and_filter_documents

def approximate_counter(text, probability=1/8):
    start_time = tm.time()
    counter = {}
    for char in text:
        if random.random() < probability:
            if char not in counter.keys():
                counter[char] = 0
            counter[char] += 1
            
    sorted_counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
    end_time = tm.time()
    return sorted_counter, end_time-start_time  

def calculate_statistics_files_all_languages(all_counters, exact_counter, a, trials):
    
    files_languages = ["en", "es", "fr"]
    
    n_events = sum(exact_counter.values())  # this is the same as the number of letters in the document... i hope...
    all_counter_sum_everything = [sum(counter.values()) for counter in all_counters]

    mean_value = calc_mean(all_counter_sum_everything, trials)
    max_dev = calc_dev(all_counter_sum_everything, mean_value)
    mad = calc_mad(all_counter_sum_everything, mean_value, trials)
    std_dev = calc_std_dev(all_counter_sum_everything, mean_value, trials)

    el = mean_value/n_events

    absolute_errors = []
    relative_errors = []

    for approx_counter in all_counters:
        absolute_error = sum(abs(exact_counter[key] - approx_counter[key]) for key in exact_counter)
        relative_error = sum(abs(exact_counter[key] - approx_counter[key]) / exact_counter[key] for key in exact_counter if exact_counter[key] != 0)

        absolute_errors.append(absolute_error)
        relative_errors.append(relative_error)

    avg_absolute_error = sum(absolute_errors) / len(absolute_errors)
    avg_relative_error = sum(relative_errors) / len(relative_errors)
    min_absolute_error = min(absolute_errors)
    min_relative_error = min(relative_errors)
    max_absolute_error = max(absolute_errors)
    max_relative_error = max(relative_errors)

    #write to file
    file_write_stats(files_languages[a], n_events, mean_value, mad, std_dev,
                    max_dev, el,
                    avg_absolute_error, avg_relative_error,
                    min_absolute_error, max_absolute_error, 
                    min_relative_error, max_relative_error)    

def incidency_stats_files_aprox(file_diff, all_counters, exact_counter, n_elements):
    # average same keys -> hit cada vez q as keys sao todas iguais em both - DONE
    # average same order 100% -> hit cada vez q as keys sao todas iguais e na mesma order - DONE
    
    # average same order 25% times -> hit cada vez q 25% keys estao na mesma order - DONE
    # average same order 50% times -> hit cada vez q 50% keys estao na mesma order - DONE
    # average same order 75% times -> hit cada vez q 75% keys estao na mesma order - DONE
    
    all_counters = [dict(list(dict_all.items())[:n_elements]) for dict_all in all_counters]
    exact_counter = dict(list(exact_counter.items())[:n_elements])
    
    all_counters_keys = [list(dict_all.keys()) for dict_all in all_counters]
    exact_counter_keys = list(exact_counter.keys())
    
    total_same_order_correspondences = sum(exact_counter_keys==element for element in all_counters_keys)
    total_same_keys_correspondence = sum(sorted(exact_counter_keys)==sorted(element) for element in all_counters_keys)
    
    avg_mean_total_hits = total_same_order_correspondences/len(all_counters_keys)
    avg_total_key_hits = total_same_keys_correspondence/len(all_counters_keys)
    
    sum_25 = compare_lists(all_counters_keys, exact_counter_keys, threshold=0.25)
    sum_50 = compare_lists(all_counters_keys, exact_counter_keys, threshold=0.50)
    sum_75 = compare_lists(all_counters_keys, exact_counter_keys, threshold=0.75)
    
    file_diff.write("k:" + str(n_elements) + "\n")
    file_diff.write("order_correspondences: " + str(avg_mean_total_hits*100) + "%\n")     
    file_diff.write("keys_correspondence: " + str(avg_total_key_hits*100) + "%\n") 
    file_diff.write("sum_25: " + str(sum_25*100/len(all_counters_keys)) + "%\n") 
    file_diff.write("sum_50: " + str(sum_50*100/len(all_counters_keys)) + "%\n") 
    file_diff.write("sum_75: " + str(sum_75*100/len(all_counters_keys)) + "%\n") 
    
def main():
    text_en, text_es, text_fr = get_and_filter_documents()

    all_texts = [text_en, text_es, text_fr]
    files_languages = ["en", "es", "fr"]
    random.seed(103453)

    file_time = open("./results/time_aproximate.txt", "w")

    for a in range(len(all_texts)):
        
        text = all_texts[a]
        # This will be repeated for all three languages
        
        exact_counter, _ = exact_counter_func(text)
        
        all_counters = []
        times = []
        trials = 100

        for i in range(trials):
            counter, time = approximate_counter(text)
            counter.update({key: 0 for key in exact_counter if key not in counter})
            all_counters.append(counter)
            times.append(time)
            
        calculate_statistics_files_all_languages(all_counters, exact_counter, a, trials)
        file_diff = open("./results/approx_counter_" + files_languages[a] + ".txt", "w")
        
        for i in [3, 5, 11]:
            incidency_stats_files_aprox(file_diff, all_counters, exact_counter, i)
        file_diff.close()
        
        # write the average of time based on all trials
        file_time.write(files_languages[a] + ": " + str(sum(times)/len(times)) +"\n")
        
    file_time.close()

if "__main__"==__name__:
    main()


    