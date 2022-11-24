from PIL import Image, ImageDraw
im = Image.new('RGB', (800,600), color=('#FAACAC'))
draw_text = ImageDraw.Draw(im)
draw_text.text(
    (400,300),
    'fhvjdjh',
    fill=('#1C0606')
    )

im.save('C:/Users/user/Documents/чтото.jpg')

