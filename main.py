import colorgram

t_colors = colorgram.extract('image.jpg', 30)

extracted_colors = [(252, 250, 247), (253, 247, 249), (237, 251, 245), (249, 228, 17), (213, 13, 9), (198, 12, 35), 
                    (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152),
                    (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), 
                    (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9),
                    (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

# extracting RGB colors from an image
""" for i in t_colors:

    extracted_color_red = i.rgb.r
    extracted_color_green = i.rgb.g
    extracted_color_blue = i.rgb.b

    extracted_color = (extracted_color_red, extracted_color_green, extracted_color_blue)

    extracted_colors.append(extracted_color)

print(extracted_colors) """

