import os
from bs4 import BeautifulSoup

def change_svg_color(input_directory, output_directory, new_color):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for root, _, files in os.walk(input_directory):
        for filename in files:
            if filename.endswith(".svg"):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r') as file:
                    svg_content = file.read()
                
                soup = BeautifulSoup(svg_content, 'xml')
                
                # Change colors for elements with 'fill' and 'stroke' attributes
                for element in soup.find_all(['path', 'rect', 'circle', 'polygon', 'ellipse', 'line', 'polyline', 'g']):
                    if 'fill' in element.attrs:
                        if element['fill'] not in ['none', 'transparent']:
                            element['fill'] = new_color
                    else:
                        element['fill'] = new_color

                    if 'stroke' in element.attrs:
                        if element['stroke'] not in ['none', 'transparent']:
                            element['stroke'] = new_color

                # Change colors in style attributes
                for style in soup.find_all(style=True):
                    style['style'] = style['style'].replace('fill:black', f'fill:{new_color}').replace('stroke:black', f'stroke:{new_color}')
                    style['style'] = style['style'].replace('fill:#000000', f'fill:{new_color}').replace('stroke:#000000', f'stroke:{new_color}')
                    style['style'] = style['style'].replace('fill:#000', f'fill:{new_color}').replace('stroke:#000', f'stroke:{new_color}')
                
                # Change colors defined in CSS
                for css in soup.find_all('style'):
                    if css.string:
                        css.string = css.string.replace('fill:black', f'fill:{new_color}').replace('stroke:black', f'stroke:{new_color}')
                        css.string = css.string.replace('fill:#000000', f'fill:{new_color}').replace('stroke:#000000', f'stroke:{new_color}')
                        css.string = css.string.replace('fill:#000', f'fill:{new_color}').replace('stroke:#000', f'stroke:{new_color}')
                
                relative_path = os.path.relpath(root, input_directory)
                output_path = os.path.join(output_directory, relative_path)
                if not os.path.exists(output_path):
                    os.makedirs(output_path)
                
                new_svg_content = str(soup)
                with open(os.path.join(output_path, filename), 'w') as file:
                    file.write(new_svg_content)

input_directory = "images/icons"
output_directory = "output"
# new_color = "#f28fac"  
new_color = "#aae9b2" 

change_svg_color(input_directory, output_directory, new_color)
