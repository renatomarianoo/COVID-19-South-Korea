import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def grouped_plots(ax):
    for i in ax:
        i.grid(True, axis='x', color='lightgrey')
        i.spines[['top', 'right', 'left']].set_visible(False)
        i.tick_params(axis='both', left=False, bottom=False)
    plt.xlabel('')


def set_month_tick():
    # Set the locator
    locator = mdates.MonthLocator()  # every month
    plt.gca().xaxis.set_major_locator(locator)

    # Specify formatter
    fmt = mdates.DateFormatter('%b')
    plt.gca().xaxis.set_major_formatter(fmt)


def clear_barplot(plot_title="", plot_xlabel="", plot_ylabel=""):

    plt.title(plot_title)
    plt.xlabel(plot_xlabel)
    plt.ylabel(plot_ylabel)

    plt.legend()
    plt.xlabel("")
    plt.ylabel("")
    plt.yticks([])
