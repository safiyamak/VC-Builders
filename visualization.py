import matplotlib.pyplot as plt
def visualize_scores(train_scores, test_scores):
    # Check if the lengths of the lists are equal
    if len(train_scores) != len(test_scores):
        raise ValueError("The lists train_scores and test_scores must have the same length.")    # Labels for each pair of bars
    labels = [
        "Problem Definitiveness",
        "Solution Actionability",
        "Scalability",
        "Societal Impact",
        "Environmental Impact",
        "Technological Innovations",
        "Financial Planning",
        "Competitiveness",
        "Adherence to Principles",
        "Founder Performance"
    ]    # Set up the figure and axes
    plt.figure(figsize=(14, 8))    # Set the positions and width for the bars
    positions = range(len(train_scores))
    bar_width = 0.35    # Plotting
    plt.bar([p - bar_width/2 for p in positions], train_scores, width=bar_width, color='blue', label='Training Scores')
    plt.bar([p + bar_width/2 for p in positions], test_scores, width=bar_width, color='green', label='Test Scores')    # Adding labels and title
    plt.xlabel('Categories')
    plt.ylabel('Scores')
    plt.title('Comparison of business ideas')
    plt.xticks(positions, labels, rotation=45, ha='right')
    plt.legend()    # Show the plot
    plt.tight_layout()
    plt.show()