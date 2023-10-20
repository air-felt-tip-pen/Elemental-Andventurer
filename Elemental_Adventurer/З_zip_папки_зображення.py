import pygame
import zipfile
import io

def load_image_from_zip(zip_file_path, image_path_in_zip):
    try:
        zip_file = zipfile.ZipFile(zip_file_path, 'r')
        image_data = zip_file.read(image_path_in_zip)
        print(image_data)
        image_surface = pygame.image.load(io.BytesIO(image_data))
        zip_file.close()
        return image_surface
    except: return None

# Приклад використання функції:
loaded_image = load_image_from_zip(zip_file_path='image.zip', image_path_in_zip='image/box_.png')
# print(loaded_image)
if loaded_image is not None:
    # Показ завантаженого зображення.
    pygame.init()
    screen = pygame.display.set_mode((loaded_image.get_width()+100, loaded_image.get_height()+100))
    screen.blit(loaded_image, (50, 50))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
