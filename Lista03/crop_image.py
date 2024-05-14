from PIL import Image

def crop(image_path, new_path):
    img = Image.open(image_path)
    width, height = img.size
    left, right = 0, width
    upper, lower = 0, height-210
    cropped_img = img.crop((left, upper, right, lower))
    cropped_img.save(new_path)


path = ".\Lista03\Report\png\CNN_Simple_history.png"
new_path = ".\Lista03\Report\png\CNN_Simple_history_cropped.png"
crop(path, new_path)

path = ".\Lista03\Report\png\MLP_history.png"
new_path = ".\Lista03\Report\png\MLP_history_cropped.png"
crop(path, new_path)

path = ".\Lista03\Report\png\ResNet_history.png"
new_path = ".\Lista03\Report\png\ResNet_history_cropped.png"
crop(path, new_path)