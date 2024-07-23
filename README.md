# SVG Color Changer ![License](https://img.shields.io/badge/License-MIT-teal.svg) 

This project provides a Python script to change the color of SVG icons. It was created to solve an issue with the Zen-weather app, needing a quick way to change SVG values to match the desired color.

![Icon-before](/assets/wi-day-sunny-before.svg)
![Icon](/assets/wi-day-sunny.svg)

## Description

The SVG Color Changer script is designed to traverse a directory of SVG files and change their fill and stroke colors to a specified color. This is particularly useful for customizing the appearance of icons to fit a specific theme or aesthetic, such as the neon purple color used in the Zen-weather app.

## Usage

### Install Dependencies

Make sure you have the required Python libraries installed. You can install them using pip:

```bash
python -m venv venv
```

```bash
pip install beautifulsoup4 lxml
```

## Running the Script

1. Place the script in a directory of your choice.
2. Update the `input_directory` variable in the script to point to the directory containing your SVG files (e.g., `images/icons`).
3. Update the `output_directory` variable in the script to specify where the modified SVG files should be saved (e.g., `output`).
4. Set the `new_color` variable to the desired color in hex format (e.g., `#D900FF` for neon purple).
5. Run the script using your Python interpreter:

```bash
python change_svg_color.py
```


