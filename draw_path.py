import requests
from PIL import Image, ImageDraw

def fetch_golf_ball_path():
    url = "http://127.0.0.1:8000/simulate_golf_ball_path"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("path")
    else:
        print(f"Failed to get response: {response.status_code}")
        return None

def draw_path_on_image(path, image_size=(1920, 1080), output_file="golf_ball_path.png"):
    # Create a blank image
    image = Image.open('/home/fm-pc-lt-234/Downloads/golf_data/valid/images_valid/folder4_video2-trimmed-_mov-0014_jpg.rf.6609c12028be9ebb16a91b087ac3a73a.jpg')

    draw = ImageDraw.Draw(image)
    
    # Draw the path
    if path:
        for i in range(len(path) - 1):
            print('path: ', i, path[i])
            draw.line((*path[i], *path[i+1]), fill=(255, 0, 0), width=3)
    
    # Save the image
    image.show()
    image.save(output_file)
    print(f"Image saved as {output_file}")

if __name__ == "__main__":
    path = fetch_golf_ball_path()
    print(path)
    if path:
        draw_path_on_image(path)
 
