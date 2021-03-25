import matplotlib.pyplot as plt

def plot_line_graph(title: str,x_axis,y_axis: dict, x_axis_name, y_axis_name):
    fig = plt.figure(figsize=(8,8))
    ax1 = fig.add_subplot(111)
    plt.title(title,fontsize = 20)
    ax1.set_ylim(0,1)
    plt.ylabel(y_axis_name,fontsize = 15)
    plt.xlabel(x_axis_name, fontsize = 15)

    ax1.scatter(x_axis, y_axis['naive'], s=50, c='b', marker="x", label='Naive-Bayes')
    ax1.plot(x_axis, y_axis['naive'], c='b')

    ax1.scatter(x_axis,y_axis['maxEnt'], s=50, c='r', marker="x", label='MaxEnt')
    ax1.plot(x_axis,y_axis['maxEnt'], c='r')

    ax1.scatter(x_axis, y_axis['svm'], s=50, c='g', marker="x", label='SVM')
    ax1.plot(x_axis,y_axis['svm'], c='g')

    plt.legend(loc='upper left');
    plt.show()
