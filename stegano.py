
from PIL import Image
import numpy
image_path= "C:/Users/Benduch/Desktop/Pyth/Aaladin.jpg"

def lsb_1(image_path,message):
    mon_image= Image.open(image_path)
    image_array=numpy.array(mon_image)

    image_array-=image_array%2 # passage de tous les pixels en valeur pair

    binary_message= [ int(bin_number) for bin_number in "".join(format(ord(i),'08b') for i in message)]# convetrt message to bianarry

    number_rows,number_cols, number_colors = image_array.shape
    index_binary_message=0
    for index_row in range(0,number_rows):
        for index_col in range(0, number_cols):
            for index_color in range(0, number_colors):
                if index_binary_message < len(binary_message):
                    image_array[index_row,index_col,index_color]+= binary_message[index_binary_message]
                else:
                    break
                index_binary_message+=1
    print(image_array)
lsb_1(image_path,"Coucou les Loulous")
