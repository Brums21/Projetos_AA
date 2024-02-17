import math

def write_to_files_stats(lang, n_events, mean_value, 
                        mad, std_dev,
                        max_dev, el,
                        avg_absolute_error, avg_relative_error,
                        min_absolute_error, max_absolute_error, 
                        min_relative_error, max_relative_error):
    
    file = open("./results/stats_aprox_" + lang +".txt", "w")
    
    file.write("Number of events: " + str(n_events) + "\n")
    file.write("Mean: " + str(mean_value) + "\n")
    file.write("mad: " + str(round(mad, 5)) + "\n")
    file.write("std_dev: " + str(round(std_dev, 5)) + "\n")
    file.write("max_dev: " + str(round(max_dev, 5)) + "\n")
    file.write("Probability: " + str(round(el*100, 2)) + "%\n")
    file.write("Average Absolute Error: " + str(round(avg_absolute_error, 5)) + "\n")
    file.write("Average Relative Error: " + str(round(avg_relative_error, 5)) + "\n")
    file.write("Minimum Absolute Error: " + str(round(min_absolute_error, 5)) + "\n")
    file.write("Minimum Relative Error: " + str(round(min_relative_error, 5)) + "\n")
    file.write("Maximum Absolute Error: " + str(round(max_absolute_error, 5)) + "\n")
    file.write("Maximum Relative Error: " + str(round(max_relative_error, 5)) + "\n")
    
    file.close()

def mean(array: [], elements: int):
    return sum(array)/elements

def dev(array: [], mean: int):
    return max(abs(value-mean) for value in array)

def mad(array: [], mean: int, n_elements: int):
    return sum(abs(value-mean) for value in array) / n_elements

def std_dev(array: [], mean: int, n_elements: int):
    return math.sqrt(sum((value-mean)**2 for value in array) / n_elements)

def sum_lists_with_same_order(list_of_lists, target_list, threshold=0.75):
    return sum(1 for sublist in list_of_lists if lists_have_same_order(sublist, target_list, threshold))

def lists_have_same_order(list1, list2, threshold):
    common_elements = sum(list1[i] == list2[i] for i in range(min(len(list1), len(list2))))
    return common_elements / len(list1) >= threshold