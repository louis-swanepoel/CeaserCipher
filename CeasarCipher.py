#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 17:00:16 2021

@author: louisswanepoel
"""
import MetricFunctions as m 

'''
#EXTRA!! Ceaser cypher module that performs decryption, encryption and autodecryption 
when the message is called as the argument in the following functions
'''
    
'''
Encryption function that returns encrypted message
Part 1
'''
 
def decrypt(cypher,rot):
    
    decrypted_message = []
    for letter in cypher:
                                
        letter = ord(letter) 
        if 65 <= letter <= 90:
            
            if (letter - rot%26) < 65 :
            
                ch = (26 + letter - 64 - (rot)%26)     
                ch = chr(ch+64)      
                decrypted_message.append(ch)
                
            elif (letter - rot%26) >= 65 :
                
                ch = (letter -65 - (rot)%26)     
                ch = chr(ch+65)      
                decrypted_message.append(ch)
                
        
            
        elif 97 <= letter <= 122:
            
            if (letter - rot%26) < 97 :
                
                ch = (26 + letter + (rot)%26)  
                ch = chr(ch+97)      
                decrypted_message.append(ch.upper())
                
            elif (letter + rot%26) <= 122 :    
                ch = (letter - 97 - (rot)%26)    
                ch = chr(ch+97)  
                decrypted_message.append(ch.upper())
                
            
        else:                              
            ch = chr(letter)
            decrypted_message.append(ch.upper())
    
    return ''.join(decrypted_message)


'''
Decryption function that returns decrypted message
Part 1
'''

def encrypt(word,rot):   
    
    encrypted_message = [] 
             
    for letter in word:
        
        letter = ord(letter)      
                    
        if 65 <= letter <= 90:
            
            if (letter + rot%26) > 90 :
            
                ch = (letter + (rot)%26) % 90    
                ch = chr(ch+64)      
                encrypted_message.append(ch)
                
            elif (letter + rot%26) <= 90 :
                
                ch = (letter + (rot)%26)     
                ch = chr(ch)      
                encrypted_message.append(ch)
                
        #EXTRA!! gives the option to add another range of ASCII values if the cipher is required to also shift punctuation 
            
        elif 97 <= letter <= 122:
            
            if (letter + rot%26) > 122 :
                
                ch = (letter + (rot)%26) % 122    
                ch = chr(ch+96)      
                encrypted_message.append(ch.upper())
                
            elif (letter + rot%26) <= 122 :    
                ch = (letter + (rot)%26)        
                ch = chr(ch)  
                encrypted_message.append(ch.upper())
                
            
        else:                              
            ch = chr(letter)
            encrypted_message.append(ch.upper())
    
    return ''.join(encrypted_message)

'''
Auto-decryption function that returns decrypted message
Part 4
'''

def auto_decrypt(encrypted_message):
    
    # Part 4 Question 2 
        
    encrypted_message_wordlist =  encrypted_message.split()
    
    if len(encrypted_message_wordlist) >= 10:
        words_to_iterate = (encrypted_message_wordlist[:10])
        
    elif len(encrypted_message_wordlist) < 10:
        words_to_iterate = encrypted_message_wordlist[:len(encrypted_message_wordlist)]
        
        
    rot_currentvalue = -1
        
    # iterating through rotations
    for rot in range(0,27):
            
        rot_currentvalue += 1  
        
        #iterating through words 
        for word in words_to_iterate:
                
            rotated_word = []            
                
            #iterating through letters
            for letter in word:
                
                
                
                    
                letter = ord(letter)
                    
                if 64 < letter < 91:
                    
                    ch = (letter - 65 - (rot)%26) % 26    
                    ch = chr(ch + 65)  
                    rotated_word.append(ch.lower())
                    
                         
                elif 96 < letter < 123:
                    
                        ch = (letter - 97 - (rot)%26) % 26    
                        ch = chr(ch + 97)  
                        rotated_word.append(ch.lower())
                    
                        
                else:                               
                    ch = chr(letter)
                    rotated_word.append(ch.lower())
            
            
            # for loop to iterate through common words and compare it to rotated word        
              
            rotated_word = ''.join(rotated_word)            
            
            with open('words.txt', 'r+') as words:
                same_word_counter = 0 
                for line in range(1,207):
                    common_word = words.readline(line)                   
                    if rotated_word == common_word.strip():
                        same_word_counter += 1                    
                        
            
            #if there is a word that matches a word in the english dictionary
            if same_word_counter >= 1:
                
                 decrypted_message = decrypt(encrypted_message, rot_currentvalue)
                 #prints the suspected correct decryption and... #EXTRA!! the key that was used the obtain it                   
                 print('\n' + decrypted_message + '\n')
                 print('Found with rotation: ' , rot_currentvalue)
                 correct_answer_question = input('Is this the correct decryption? Y/N ')
                
                 if correct_answer_question == 'Y':
                    #the fuNCtion has found the correct decryption and so writes the word metrics and plots the graph of word frequency  
                    m.repeated_word_graph(decrypted_message) 
                    m.metrics(decrypted_message)
                    return "End of Programme"
                
                 elif correct_answer_question == 'N':
               
                         print('autodecryption programming RELOADING...')
                
            
                
                 
                    
                        
                
                
                    
            
            
             
                    
            
           
        
       
        

        
        
        
        
        
        
        
        
        
    
    