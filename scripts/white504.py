from PIL import Image

# Create a new image with the desired size
image = Image.new('RGB', (504, 504), color='red')
for _ in ['1']:
# Save the image
    image.save('/home/hangyuan/nx/code/BSRN/datasets/Set5/gt0/'+_+'.png')
