#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 17:50:04 2021

@author: louisswanepoel
"""
import operator
import string
'''
#EXTRA!! Module that returns the metrics of a sentence when the sentence is used as an argument for the metrics function
'''


'''
Functions that calculate and return metric data
'''

# Question 2.3 & 2.4 word frequency list
def repeated_word_table(sorted_word_frequency_d):   
    
    return  [list(words) for words in sorted_word_frequency_d]   
                 
def repeatedwordinfo(sorted_word_frequency_d): 
    
    list_word_and_F = [list(words) for words in sorted_word_frequency_d] 
    list_words = [word[0] for word in list_word_and_F]    
    list_F = [F[1] for F in list_word_and_F]     
    if len(list_words) <= 5 :
        return list_words       
    elif len(list_words) >= 5 :      
        counter = 0
        for f in list_F:            
            if f == list_F[counter - 1]:
                while (counter-1)<=5:
                    return list_words[:(counter -1)]
            counter += 1

# Question 2.2 most common letter
def most_common_letter(decrypted_message):   
    
    d = {}    
    for letter in decrypted_message:
        if (64 < ord(letter) < 90):
            if letter in d:               
                d[letter] += 1
            else:
                d[letter] = 1
        elif 96 < ord(letter) < 123:
             if letter in d: 
                 d[letter] += 1
             else:
                d[letter] = 1   
                       
    return max(d, key = d.get)

# Question 2.2 minimum word length    
def minimumwordlength(sorted_word_length_d): 
    
    length_of_shortest_word = len(min(sorted_word_length_d, key = sorted_word_length_d.get))
    return length_of_shortest_word

# Question 2.2 maximum word length
def maximumwordlength(sorted_word_length_d): 
        
    length_of_longest_word = len(max(sorted_word_length_d, key = sorted_word_length_d.get))
    return length_of_longest_word
                                                 

'''
Function that first finds suitable arguments for the metrics functions and then writes all metrics to metrics.txt
Part 2
'''


def metrics(decrypted_message):
    
    
    # redifines the decrypted words as a string with no numbers in it 
    decrypted_message = ''.join([ch for ch in decrypted_message if not ch.isdigit()])
    decrypted_message = decrypted_message.translate(str.maketrans('', '', string.punctuation))
    
    #creates a list of words in the message 
    decrypted_word_list = decrypted_message.split()
    
    word_frequency_d= {}       
    for word in decrypted_word_list:
        #creates a dictionary with values that correspond to word frequency 
        if word not in word_frequency_d:               
            word_frequency_d[word] = 1
        else:
            word_frequency_d[word] += 1
           
    sorted_word_frequency_d = sorted(word_frequency_d.items(), reverse=True ,key=operator.itemgetter(1))
    
    unique_words = set(decrypted_word_list)
    
    sorted_word_length_d = {}
    for word in decrypted_word_list:
        sorted_word_length_d[word] = len(word)
        
    with open("metrics.txt:", "w+" ) as fi:
                    
                        # 2.2, 2.1 number of words in the message 
                        counter = 0
                        for word in decrypted_word_list:                            
                            counter += 1
                        fi.write('Total number of words: ' + str(counter)+'\n')
                       
                        # 2.2,2.1 number of unique words in the message                         
                        counter = 0
                        for words in unique_words:
                            counter += 1
                        fi.write('Number of unique words: ' + str(counter)+'\n')
                        
                        # Question 2.2 minimum word length      
                        fi.write('Minimum word length: ' + str(minimumwordlength(sorted_word_length_d))+'\n')
                        
                        # Question 2.2 maximum word length
                        fi.write('Maximum word length: '+ str(maximumwordlength(sorted_word_length_d)) + '\n')
                                                                                                  
                        # Question 2.2 most common letter                     
                        fi.write('Most common letter: ' + str(most_common_letter(decrypted_message))+'\n')
                        
                        # Question 2.3 & 2.4 word frequency list
                        fi.write(str(repeatedwordinfo(sorted_word_frequency_d)))
                        fi.write('\n')
                        list_word_and_F = repeated_word_table(sorted_word_frequency_d)
                        
                        #formatting to create tabular form of word and word frequency
                        for word_frequency in  list_word_and_F :
                            list_of_words_and_frequencies = str('\n' + str(word_frequency[0])+ ': ' + str(word_frequency[1]) )                            
                            fi.write(list_of_words_and_frequencies)
                            


'''
#EXTRA!!
Function that plots a bar chart of word against word frequency
Part 5
'''

                       
def repeated_word_graph(decrypted_message):
        
     import matplotlib.pyplot as plt
     import numpy as np
     
     decrypted_message = ''.join([ch for ch in decrypted_message if not ch.isdigit()])
     decrypted_message = decrypted_message.translate(str.maketrans('', '', string.punctuation))
     decrypted_word_list = decrypted_message.split()
     word_frequency_d = {}
     for word in decrypted_word_list:
        #creates a dictionary with values that correspond to word frequency 
        if word not in word_frequency_d:               
            word_frequency_d[word] = 1
        else:
            word_frequency_d[word] += 1
               
     sorted_word_frequency_d = sorted(word_frequency_d.items(), reverse=True ,key=operator.itemgetter(1)) 
     list_word_and_F = repeated_word_table(sorted_word_frequency_d)
     
     list_words = [item[0] for item in list_word_and_F][:5]  
     list_F = [item[1] for item in list_word_and_F][:5] 
     x_pos = np.arange(len(list_words))
     plt.bar(x_pos, list_F)
     plt.xticks(x_pos, list_words)
     
     
     #formatting of the bar chat     
     plt.xlabel('Word')
     plt.ylabel('Word Frequency', color = '#EEEEEE')
     plt.title('Word Frequency Against Word' ,color = '#EEEEEE')
     plt.tight_layout()
     
     plt.plot()
     
     
     
      
    
                            
                            
                            
                       
                       
        




                        