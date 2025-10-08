#Lists support the slice notation that allows you to get a sublist from a list:
# sub_list = list[begin: end: step]
'''The (begin) index defaults to zero. 
The (end) index defaults to the length of the list. And the (step) index defaults to 1.

The slice will start from the begin up to the end in the step of step.'''

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors1=colors[:3]
sub_colors2=colors[-3:]
print(sub_colors1)
print(sub_colors2)


# retriving every nth element from a list
sub_colors3 = colors[::2]
print(sub_colors3)