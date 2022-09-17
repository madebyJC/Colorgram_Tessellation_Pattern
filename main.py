import colorgram

rgb_colors = []
colors = colorgram.extract('Tessellation Pattern.png', 9)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)
