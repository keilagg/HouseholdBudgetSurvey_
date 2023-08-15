

# Geting percentage with dictionary


# Median percentage of transportantion expenses over total expenses
transpExpense = []
totalExpense_perc = []
for year in df_dict_keys:
    expensesTransp = dict_df_popExpenses_all[year][transport_codes].sum(axis=1) # Get sum all transp. expenses
    expensesTrransp_yearly = expensesTransp.sum() # get yearly spending
    percentage_s = (expensesTransp / dict_df_popExpenses_all[year]['GASTOMON']) * 100 # Get % on total expenses
    percentage_ = percentage_s.median() # Get median of population percentages 
    transpExpense.append(expensesTrransp_yearly)
    totalExpense_perc.append(percentage_)
plt.bar(df_dict_keys, totalExpense_perc );


# Better visualization
fig.tight_layout()
fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange', 'pu']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(df_dict_keys, transpExpense, label = bar_labels, color=bar_colors)

ax.set_ylabel('Total Spent (€)')
ax.set_title('Total Expense in transportation 2018-2022')

# Improve grid settings
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_color('#DDDDDD')

# Remove ticks
ax.tick_params(bottom=False, left=False)

# Set grid
ax.set_axisbelow(True)
ax.yaxis.grid(True)
ax.xaxis.grid(False)

# Better visualization
fig.tight_layout()


# Median percentage of transportantion expenses over total expenses
transpExpense = []
totalExpense_perc = []
for year in df_dict_keys:
    expensesTransp = dict_df_popExpenses_all[year][transport_codes].sum(axis=1) # Get sum all transp. expenses
    expensesTrransp_yearly = expensesTransp.sum() # get yearly spending
    percentage_s = (expensesTransp / dict_df_popExpenses_all[year]['GASTOMON']) * 100 # Get % on total expenses
    percentage_ = percentage_s.median() # Get median of population percentages 
    transpExpense.append(expensesTrransp_yearly)
    totalExpense_perc.append(percentage_)
plt.bar(df_dict_keys, totalExpense_perc );