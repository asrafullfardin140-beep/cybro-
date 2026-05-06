from PIL import Image

def make_white_logo(input_path, output_path):
    # Open the image and ensure it has an alpha channel
    img = Image.open(input_path).convert("RGBA")
    data = img.getdata()

    new_data = []
    for item in data:
        # item is (R, G, B, A)
        # If the pixel is not fully transparent, make it white but keep its alpha
        # For anti-aliased edges, we just set RGB to 255 and keep the original alpha
        if item[3] > 0:
            new_data.append((255, 255, 255, item[3]))
        else:
            new_data.append((255, 255, 255, 0))

    img.putdata(new_data)
    img.save(output_path, "PNG")
    print(f"Saved {output_path}")

make_white_logo("/Users/asrafullfardin/.gemini/antigravity/playground/primordial-galileo/logo_site.png", "/Users/asrafullfardin/.gemini/antigravity/playground/primordial-galileo/logo_white_exact.png")
