import matplotlib.pyplot as plt

def plot_line(x, y, title=None, xlabel=None, ylabel=None):
    plt.plot(x, y)
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    plt.show()

def plot_scatter(x, y, title=None, xlabel=None, ylabel=None):
    plt.scatter(x, y)
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    plt.show()

def plot_histogram(data, bins=10, title=None, xlabel=None, ylabel=None):
    plt.hist(data, bins=bins)
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    plt.show()

def plot_bar(labels, values, title=None, xlabel=None, ylabel=None):
    plt.bar(labels, values)
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    plt.show()

def plot_pie(labels, sizes, title=None):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    if title:
        plt.title(title)
    plt.show()