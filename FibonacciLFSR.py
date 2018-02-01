# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 18:05:11 2017

@author: Abhigyan
"""

"""********Fibonacci LFSR's********"""

"""Takes in a particular state of Fibonacci LFSR, the taps and length of the LFSR and returns the next state"""
def updateFLFSR(state, taps, length):                                 #Takes in current state as decimal,taps as a tuple and length of the LFSR bitstream
      updateBit = 0                                                   
      
      for i in taps:
            updateBit = updateBit ^ (state << (i - 1))                #Finds the next input bit
      updateBit = updateBit & (1 << (length - 1))                     #Shifts the XORbit to the 1st position
      lfsrNextState = ((state >> 1) | updateBit)  
      
      return lfsrNextState                                            #Returns the next state of LFSR as a decimal number
       
"""END"""
