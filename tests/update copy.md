# sablepy.Subplots

- Methods:
  - [`make_subplot`](#make-subplot)
  - [`set_plot_title`](#set-plot-title)
  - [`set_subplot_title`](#set-subplot-title)
  - [`set_subplot_xaxis`](#set-subplot-xaxis)
  - [`set_subplot_yaxis`](#set-subplot-yaxis)
- Examples:
  - [Basic Usage](#basic-usage)
  - [Customization](#subplot-customization)

## Methods

<strong id='set-plot-title'>set_plot_title</strong>(<b>text</b>)

> Parameters

<ul style='list-style: none'>
    <li>
        <b>text : <i>str</i></b>
        <ul style='list-style: none'>
            <li>String expression of title text.</li>
        </ul>
    </li>
    <li>
        <b>number : <i>float|int</i></b>
        <ul style='list-style: none'>
            <li>Number of subplot title text.</li>
        </ul>
    </li>

</ul>
<hr>

<strong id='set-subplot-title'>set_subplot_title</strong>(<b>plot_num</b>, <b>text</b>)

> Parameters

<ul style='list-style: none'>
    <li>
        <b>plot_num : <i>int</i></b>
        <ul style='list-style: none'>
            <li>Integer representing subplot title to change.</li>
        </ul>
    </li>
    <li>
        <b>text : <i>str</i></b>
        <ul style='list-style: none'>
            <li>String expression of subplot title text.</li>
        </ul>
    </li>

</ul>
<hr>

<strong id='set-subplot-xaxis'>set_subplot_xaxis</strong>(<b>plot_num</b>, <b>text</b>)

> Parameters

<ul style='list-style: none'>
    <li>
        <b>plot_num : <i>int</i></b>
        <ul style='list-style: none'>
            <li>Integer representing subplot x-axis text to change.</li>
        </ul>
    </li>
    <li>
        <b>text : <i>str</i></b>
        <ul style='list-style: none'>
            <li>String expression of subplot x-axis text.</li>
        </ul>
    </li>
</ul><hr>
<strong id='set-subplot-yaxis'>set_subplot_yaxis</strong>(<b>plot_num</b>, <b>text</b>)

> Parameters

<ul style='list-style: none'>
    <li>
        <b>plot_num : <i>int</i></b>
        <ul style='list-style: none'>
            <li>Integer representing subplot y-axis text to change.</li>
        </ul>
    </li>
    <li>
        <b>text : <i>str</i></b>
        <ul style='list-style: none'>
            <li>String expression of subplot y-axis text.</li>
        </ul>
    </li>
</ul>
<hr>

## Examples

#### Basic Usage

```
d = Data("example")

vo2 = d.get_channel_data("vo2")
fig1 = TimeSeries(vo2)

vco2 = d.get_channel_data("vco2")
fig2 = TimeSeries(vco2)

subplot = make_subplot([fig1, fig2])
subplot.show()
```

<p align="center">
<img src="../images/subplot/subplot-basic.png" />
</p>

## Customization

- [Title](#title)
- [Subplot Titles](#subplot-titles)

### Title

- The title can be set on creation or modified after:
  ```
  subplot = make_subplot([fig1, fig2], plot_title='Example Plot Title')
  subplot.show()
  ```
  ```
  subplot.set_plot_title('Example Plot Title')
  ```

<p align="center">
<img src="../images/subplot/subplot-plotTitle.png" />
</p>

### Subplot Titles

- Similar to `plot_title`, subplot titles can be set on creation or modified after
- `subplot_titles` can either be a string expression, or a list of string expressions:

  #### Using a string expression

  - If given a string, the subplot title to change is defined by `title_first_subplot`, which is False by default. The following example would change the second subplot's title:

    ```
    subplot = make_subplot([fig1, fig2], subplot_titles='Example Subplot Title')
    ```

    <p align="center">
    <img src="../images/subplot/subplot-subplotTitle-default.png" />
    </p>

  - We can title the first subplot with a string argument using `title_first_subplot=True`:

    ```
    subplot = make_subplot([fig1, fig2], subplot_titles='Example Subplot Title', title_first_subplot=True)
    ```

    <p align="center">
    <img src="../images/subplot/subplot-subplotTitle-str.png" />
    </p>

    #### Titling multiple subplots

    - A list of string expressions can be used to title multiple subplots:
      ```
      subplot = make_subplot([fig1, fig2, fig3], subplot_titles=['Subplot #2 Title', 'Subplot #3 Title'])
      ```
      - The title for subplot #1 is skipped unless `title_first_subplot=True`

    <p align="center">
    <img src="../images/subplot/subplot-subplotTitle-list.png" />
    </p>

    - Alternatively, providing as many string expressions as there are subplots will set a title for each plot:
      ```
      subplot = make_subplot([fig1, fig2, fig3], subplot_titles=['Subplot #1 Title','Subplot #2 Title','Subplot #3 Title'])
      ```

    <p align="center">
    <img src="../images/subplot/subplot-subplotTitle-list-2.png" />
    </p>

    #### Changing specific subplot title

    - You can also change the title of a specific subplot:

    ```
    subplot.set_subplot_title(2, 'Example Plot Title')
    ```

    <p align="center">
    <img src="../images/subplot/subplot-subplotTitle-setSubplotTitle.png" />
    </p>

### Subplot Axes

- Subplot axes can be customized using a variety of parameters

  #### X-Axis

  - The x-axis is shared by default (`shared_xaxes=True`) and the label is determined by the x-axis label of the first plot provided.
  - Setting `shared_xaxes=False` will allow you to individually label each x-axis using `set_subplot_xaxis`:
