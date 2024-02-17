# Projeto Algoritmos Avançados #3

Most frequent letters

## Purpose

This project presents an overview of the counting elements in a stream of data, that is, how many different elements of a given type there are in an extensive dataset. Different approaches to calculate the most frequent letters in different literacy works are performed in order to identify and characterize the different characteristics between them.

Different approaches to solve this problem were implemented:

### Exact counter: 

An implementation of a simple exact counter, in which each character from the data stream is counter and added to a data structure which stores the letter and the amount of times that letter was detected. The most frequent letters in this case correspond to the entries that have a greater number of hits detected.

### Approximate counter: 

An implementation of a counter that only counts an element if a certain probability is hit, that is, an algorithm that, in a similar way to the exact counter, tries to count elements, except it only does so when a random number is within a threshold, and therefore, the characters are only counted within a certain probability. Therefore, the overall amount of elements counts should be close to the fixed probability defined multiplied by the total number of characters in the data stream.

### Space-saving counter: 

An implementation of the _Metwally et al._ (Space-Saving) Algorithm in which only the top k elements are considered. In this algorithm, the data structure which stores the number of hits of each letter never surpasses the _k_ letters.

## How to run tests (Windows):

1. ```python3 -m venv venv```

2. ```.\venv\Scripts\activate```

3. ```pip install -r .\requirements.txt```

4. ```.\ProjetoAA.py```

### Results

Test results are presented in the `./results` directory.

### Graphics

Generated graphics are presented in the `./images` directory

### Literacy works

To count the most frequent letters, the literary work ***The Odyssey*** was downloaded from [Project Guttenberg](https://www.gutenberg.org/) in three different languages: English, Spanish and French. Then, all stopwords and non-alphabetic characters (including spaces) were removed and transformed to upper case.


