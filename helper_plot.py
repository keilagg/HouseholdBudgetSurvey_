#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 19:27:15 2023

@author: keilagonzalez
"""
import pandas as pd
from matplotlib import pyplot as plt

# Define function to plot

def plot2print(x:list, y:list, b_colors:list, ylabel:str, title:str):
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
    #ax.ticklabel_format(useOffset=False)

    # Move scientific notation 
    #t = ax.yaxis.get_offset_text()
    #t.set_fontsize(10)
    #t.set_x(0)

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



# plot share of income spent on car usage

def scatter_plot(dict_df, year):
# set bench values
    transport_expenditure = 15 # 15% of total income spent in transportation
    median_income = dict_df[year]['IMPEXAC'].median()

    groups_list = []

    #variables
    x = dict_df[year]['IMPEXAC']
    y = dict_df[year]['percentage_income']

    dict_x_conditions = [x.where(x <= median_income), 
                        x.where(x > median_income),
                        x.where(x <= median_income),
                        x.where(x > median_income)
                    ]

    dict_y_conditions = [y.where(y <= transport_expenditure), 
                    y.where(y <= transport_expenditure),
                    y.where(y > transport_expenditure),
                    y.where(y > transport_expenditure)
                    ]
    fig, ax = plt.subplots()

    colors = ['#fd8d3c', '#fecc5c', '#2c7fb8', '#253494']
    legend_ = ['Low Income, Low Costs',
            'Higher Income, Low Costs',
            'Low Income, High Costs',
            'Higher Income, High Costs'
            ]
    s = 10

    # Plot
    for i in range(len(colors)):
                            ax.scatter(dict_x_conditions[i], 
                            dict_y_conditions[i], 
                            s = s,
                            c = colors[i], 
                            alpha = .3)
    
                            values_list = [dict_x_conditions[i], dict_y_conditions[i] ]
                            groups_list.append(values_list)

    # Benchmark Mean values          
    ax.axhline(y = transport_expenditure, color = 'red', linewidth=1)           
    ax.axvline(x = median_income, color = 'red', linewidth = 1);

    ax.legend(legend_)
    plt.title(year)
    plt.show()
    return groups_list