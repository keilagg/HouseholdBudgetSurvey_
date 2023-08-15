#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 19:27:15 2023

@author: keilagonzalez
"""



# Define function to plot

def plot2print(b_colors:list, x:list, y:list, ylabel:str, title:str):
    fig, ax = plt.subplots()    
    
    # Style
    hfont = {'fontname':'Helvetica'}


    # Plot
    ax.bar(x, 
            y,  
            color=b_colors,
            edgecolor='black')
    
    # titles
    ax.set_ylabel(ylabel,  **hfont)
    ax.set_title(title, **hfont, y=1.08)

    # Move scientific notation 
    t = ax.yaxis.get_offset_text()
    t.set_fontsize(10)
    t.set_x(0)

    # Improve grid settings
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#525252')

    # Remove ticks
    ax.tick_params(bottom=False, left=False)

    # Set grid
    ax.set_axisbelow(True)
    ax.yaxis.grid(True)
    ax.xaxis.grid(False)

    # Better visualization
    fig.tight_layout()