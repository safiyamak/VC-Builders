import matplotlib.pyplot as plt
import numpy as np# Sample data for training and test sets across different dimensions
# Replace these with your actual data
dimensions = ['Dimension 1', 'Dimension 2', 'Dimension 3', 'Dimension 4']
training_scores = [80, 90, 70, 85]
test_scores = [75, 88, 65, 80]# Setting the positions and width for the bars
pos = list(range(len(dimensions)))
width = 0.4# Plotting the bars
fig, ax = plt.subplots(figsize=(10, 6))# Create a bar with training data,
# in position pos,
plt.bar(pos,
        # using training_scores data,
        training_scores,
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='b',
        # with label the first value in dimensions
        label=dimensions[0])# Create a bar with test data,
# in position pos + width,
plt.bar([p + width for p in pos],
        # using test_scores data,
        test_scores,
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='r',
        # with label the second value in dimensions
        label=dimensions[1])# Set the y axis label
ax.set_ylabel('Scores')# Set the chart's title
ax.set_title('Test and Training Data Comparison')# Set the position of the x ticks
ax.set_xticks([p + 0.5 * width for p in pos])# Set the labels for the x ticks
ax.set_xticklabels(dimensions)# Setting the x-axis and y-axis limits
plt.xlim(min(pos) - width, max(pos) + width * 2)
plt.ylim([0, max(training_scores + test_scores) * 1.1])# Adding the legend and showing the plot
plt.legend(['Training Data', 'Test Data'], loc='upper left')
plt.grid()
plt.show()