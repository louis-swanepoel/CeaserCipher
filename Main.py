#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 17:16:01 2021

@author: louisswanepoel
"""
import CeasarCipher as c
import MetricFunctions as m
import random as r

# =============================================================================
# Manual message input
# Part 1
# =============================================================================



#error message Q1.3
while True:
        message_entry_mode = input('for manual message input type [m]. for text file input type [f]: ')
        if message_entry_mode == 'm' or  message_entry_mode =='f':       
            break
else:
    print("error \n please enter information again...")  

if message_entry_mode == 'm':
    
    #error message Q1.3
    while True:
        
        cipher_mode = input("type [E] to encrypt, [D] to decrypt and [A] to auto-decrypt: ")
        if cipher_mode =='E' or cipher_mode =='D' or cipher_mode =='A':
            break
    else:
        print("error \n please enter information again...")       
    # =============================================================================
    #     ENCRYPTION
    # =============================================================================
    
    if cipher_mode == "E":
                
                # Functions for encryption and metrics collection are called after rotation is defined
            
                decrypted_message = input('please enter your message: ')
                #error message Q1.3
                while True:
                    rotation_mode = input('Would you like to enter your own integer value [M] as the ROTATION or generate a random ROTATION [R]? ')
                    if rotation_mode == 'M' or rotation_mode == 'R' :    
                        break
                else:
                    print("error \n please enter information again...")
        
                if rotation_mode == 'M':
                    
                    try:
                        rotation = int(input('what is your ROTATION value? '))
                        
                    except:
                        print("error \n please enter integer value for rotation...")
                        
                    # encrypted_message =                    
                    print(c.encrypt(decrypted_message,rotation) )
                    m.metrics(decrypted_message)
                    m.repeated_word_graph(decrypted_message)
                    
                elif rotation_mode == 'R':
                    
                    rotation = r.randint(1,26)
                    encrypted_message = c.encrypt(decrypted_message,rotation) 
                    print(encrypted_message)
                    m.metrics(decrypted_message)
                    m.repeated_word_graph(decrypted_message)
                    
    # =============================================================================
    #     DECRYPTION     
    # =============================================================================
                    
    elif cipher_mode == 'D':
            
                # Functions for decryption and metrics collection are called after rotation is defined
                
                cipher = input('please enter your cipher: ')
                #error message Q1.3
                while True:
                     rotation_mode = input('Would you like to enter your own integer value M as the ROTATION or generate a random ROTATION [R]? ')       
                     if rotation_mode == 'M' or rotation_mode == 'R' : 
                         break
                else:
                    print("error \n please enter information again...") 
                
                if rotation_mode == 'M':
                    
                    try:
                        rotation = int(input('what is your ROTATION value? '))
                        
                    except:
                        print("error \n please enter integer value for rotation...")
                    
                    decrypted_message = c.decrypt(cipher, rotation )
                    print(decrypted_message)
                    m.metrics(decrypted_message)
                    m.repeated_word_graph(decrypted_message)
                    
                elif rotation_mode == 'R':
                    
                    rotation = r.randint(1,26)
                    decrypted_message = c.decrypt(cipher, rotation )
                    print(decrypted_message)
                    m.metrics(decrypted_message)
                    m.repeated_word_graph(decrypted_message)

    # =============================================================================
    # AUTODECRYPTION                    
    # =============================================================================

    elif cipher_mode == 'A':
        
        # Function for autodecryption is called 
        
        encrypted_message = input('please enter your cipher: ')
        print(c.auto_decrypt(encrypted_message))
        
                             

# =============================================================================
# Message from a file
# Part 3                
# =============================================================================


elif message_entry_mode == 'f':
    
    
    
    text_file = input('enter the name of your text file (include file directory): ')
              
    try:
        with open( text_file , 'r+') as t:
            user_input = t.read()
    except:
        print('Sorry, file ' + text_file + ' could not be found')
    
    
    #error message Q1.3
    while True:
        
        cipher_mode = input("type [E] to encrypt, [D] to decrypt and [A] to auto-decrypt: ")
        if cipher_mode =='E' or cipher_mode =='D' or cipher_mode =='A':
            break
    else:
        print("error \n please enter information again...")
    # =============================================================================
    #     ENCRYPTION
    # =============================================================================
    
    if cipher_mode == "E":
                    
                    
                        decrypted_message = user_input
                        m.metrics(decrypted_message)
                        m.repeated_word_graph(decrypted_message)
                        #error message Q1.3
                        while True:
                            rotation_mode = input('Would you like to enter your own integer value [M] as the ROTATION or generate a random ROTATION [R]? ')
                            if rotation_mode == 'M' or rotation_mode == 'R' :    
                                break
                            else:
                                print("error \n please enter information again...")
                        
                
                        if rotation_mode == 'M':
                            try:
                                rotation = int(input('what is your ROTATION value? '))
                        
                            except:
                                print("error \n please enter integer value for rotation...")                            
                            
                            print(c.encrypt(decrypted_message,rotation) )
                           
                            
                        elif rotation_mode == 'R':
                            
                            rotation = r.randint(1,26)
                            print(c.encrypt(decrypted_message,rotation))
                                                        
                              
    # =============================================================================
    #     DECRYPTION     
    # =============================================================================
                      
    elif cipher_mode == 'D':
                        
                        cipher = user_input
                        #error message Q1.3
                        while True:
                            rotation_mode = input('Would you like to enter your own integer value [M] as the ROTATION or generate a random ROTATION [R]? ')
                            if rotation_mode == 'M' or rotation_mode == 'R' :    
                                break
                            else:
                                print("error \n please enter information again...") 
                        
                        if rotation_mode == 'M':
                            try:
                                rotation = int(input('what is your ROTATION value? '))
                        
                            except:
                                print("error \n please enter integer value for rotation...")
                            
                            decrypted_message = c.decrypt(cipher, rotation )
                            print(decrypted_message)
                            m.metrics(decrypted_message)
                            m.repeated_word_graph(decrypted_message)
                            
                        elif rotation_mode == 'R':
                            
                            rotation = r.randint(1,26)
                            decrypted_message = c.decrypt(cipher, rotation )
                            print(decrypted_message)
                            m.metrics(decrypted_message)
                            m.repeated_word_graph(decrypted_message)
                
    # =============================================================================
    # AUTODECRYPTION                    
    # =============================================================================

    elif cipher_mode == 'A':
        
        encrypted_message = user_input
        print(c.auto_decrypt(encrypted_message))
        
        
          
        
         
    
    
                
    
    
    
                    