from PIL import Image, ImageDraw
import os

# Android icon sizes (in pixels)
ICON_SIZES = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192,
    'mipmap-anydpi-v26': 192,  # Adaptive icon
}

# Adaptive icon background sizes (in pixels)
ADAPTIVE_BG_SIZES = {
    'mipmap-mdpi': 108,
    'mipmap-hdpi': 162,
    'mipmap-xhdpi': 216,
    'mipmap-xxhdpi': 324,
    'mipmap-xxxhdpi': 432,
}

def create_adaptive_icon_background(size):
    """Create a white circular background for adaptive icons"""
    bg = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(bg)
    # Draw a white circle
    draw.ellipse([(0, 0), (size, size)], fill=(255, 255, 255, 255))
    return bg

def generate_icons(source_path, output_dir):
    """Generate Android icons of various sizes"""
    try:
        # Create output directories
        for size in ICON_SIZES.keys():
            os.makedirs(os.path.join(output_dir, size), exist_ok=True)

        # Create assets/images directory if it doesn't exist
        assets_dir = os.path.join(os.path.dirname(source_path))
        os.makedirs(assets_dir, exist_ok=True)

        # Open source image
        with Image.open(source_path) as img:
            # Convert to RGBA if not already
            if img.mode != 'RGBA':
                img = img.convert('RGBA')

            # Generate regular icons
            for folder, size in ICON_SIZES.items():
                resized = img.resize((size, size), Image.Resampling.LANCZOS)
                output_path = os.path.join(output_dir, folder, 'ic_launcher.png')
                resized.save(output_path, 'PNG')
                print(f"Generated {folder}/ic_launcher.png ({size}x{size})")

            # Generate adaptive icon backgrounds
            for folder, size in ADAPTIVE_BG_SIZES.items():
                bg = create_adaptive_icon_background(size)
                output_path = os.path.join(output_dir, folder, 'ic_launcher_background.png')
                bg.save(output_path, 'PNG')
                print(f"Generated {folder}/ic_launcher_background.png ({size}x{size})")

            # Generate adaptive icon foregrounds (same as regular icons)
            for folder, size in ADAPTIVE_BG_SIZES.items():
                resized = img.resize((size, size), Image.Resampling.LANCZOS)
                output_path = os.path.join(output_dir, folder, 'ic_launcher_foreground.png')
                resized.save(output_path, 'PNG')
                print(f"Generated {folder}/ic_launcher_foreground.png ({size}x{size})")

            # Generate the main adaptive icon background for app.json
            bg = create_adaptive_icon_background(1024)  # Large size for high quality
            bg_path = os.path.join(assets_dir, 'icon_background.png')
            bg.save(bg_path, 'PNG')
            print(f"Generated main adaptive icon background: {bg_path}")

        print("\nAll icons generated successfully!")
        print(f"Output directory: {output_dir}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define paths relative to the script
    source_icon = os.path.join(script_dir, '../assets/images/icon.png')
    output_dir = os.path.join(script_dir, '../android/app/src/main/res')
    
    # Generate icons
    generate_icons(source_icon, output_dir) 