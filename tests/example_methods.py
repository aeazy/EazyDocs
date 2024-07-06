def make_subplot(
    plots: list[str],
    rows: int = None,
    cols: int = None,
    plot_title: str = None,
    subplot_titles: str | list[str] = None,
    title_first_subplot: bool = False,
    shared_xaxes: bool = True,
    shared_yaxes: bool = False,
    shared_legend: bool = True,
    show_grid: bool = False,
    plot_width: int = 1400,
    plot_height: int = 600,
    vertical_spacing: float = 0.1,
) -> None:
    """Creates a single figure containing multiple subplots.

    Args:
        plots (list[BarPlot  |  Figure  |  TimeSeries]): List of objects representing the subplots to create.
            Accepted objects include: sablepy.BarPlot | plotly.Figure | sablepy.TimeSeries
        rows (int, optional): Number of rows the plot will have. Defaults to None.
            If 'rows=None', the number of rows generated is determined by the objects passed
            to the 'plots' argument.
                sablepy.TimeSeries | plotly.Figure - one subplot per row.
                sablepy.BarPlot - two subplots per row.
        cols (int, optional): Number of cols the plot will have. Defaults to None.
            If 'cols=None', the number of cols is determined using the logic defined in 'rows' parameter.
        plot_title (str, optional): String expression representing the plot title. Defaults to None.
        subplot_titles (str  |  list[str], optional): Subplot titles. Defaults to None.
            This assumes the first subplot is not labelled unless defined otherwise by 'title_first_subplot'.
        title_first_subplot (bool, optional): Whether or not the first subplot is titled with
            the argument provided to 'subplot_titles'. Defaults to False.
        shared_xaxes (bool, optional): Whether or not the subplots all have the same x-axis. Defaults to True.
        shared_yaxes (bool, optional): Whether or not the subplots all have the same y-axis. Defaults to False.
        shared_legend (bool, optional): Whether or not the subplots should share a legend. Defaults to True.
        show_grid (bool, optional): Whether or not the subplots have grids visible. Defaults to False.
        plot_width (int, optional): The overall plot width. Defaults to 1400.
        plot_height (int, optional): The overall plot height. Defaults to 600.
        vertical_spacing (float, optional): The spacing between subplots. Defaults to 0.1.
    """

    ...


def set_plot_title(self, text: str, text2: float | int = 1.1) -> None:
    """_summary_

    Args:
        text (str): _description_
    """

    ...
