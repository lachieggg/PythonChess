import os
import pygame

def clean_image(filepath):
    """Sharpen edges by thresholding the alpha channel using pygame"""
    print(f"Processing {filepath}...")
    surface = pygame.image.load(filepath).convert_alpha()
    width, height = surface.get_size()
    
    # Process pixels
    for x in range(width):
        for y in range(height):
            color = surface.get_at((x, y))
            r, g, b, a = color
            
            # Threshold alpha: make it either 0 or 255
            if a < 128:
                new_a = 0
            else:
                new_a = 255
                
            surface.set_at((x, y), (r, g, b, new_a))

    pygame.image.save(surface, filepath)

def main():
    assets_dir = 'assets/'
    pygame.display.init()
    pygame.display.set_mode((1, 1), pygame.HIDDEN)
    
    for filename in os.listdir(assets_dir):
        # ONLY modify white pieces as requested
        if filename.startswith('W') and filename.endswith('.png'):
            filepath = os.path.join(assets_dir, filename)
            clean_image(filepath)
    
    pygame.quit()

if __name__ == "__main__":
    main()
