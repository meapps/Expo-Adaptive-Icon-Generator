# Expo Adaptive Icon Generator

A Python script for generating adaptive icon assets for your Expo projects. This tool helps you create the required foreground and background images that comply with Android’s adaptive icon guidelines, ensuring your app looks great on all devices.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Integration with Expo](#integration-with-expo)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Adaptive icons were introduced in Android 8.0 (API level 26) to support dynamic icon shapes. This Python script enables you to generate icon assets—foreground images with the correct dimensions and safe zones—ready to be used in your Expo app configuration. Whether you’re creating a new app or updating an existing one, this script simplifies the asset generation process.

## Features

- **Automatic Asset Generation:** Automatically creates icon assets in multiple resolutions for MDPI, HDPI, XHDPI, XXHDPI, and XXXHDPI.
- **Guideline Compliance:** Generates images that adhere to Android adaptive icon specifications, including proper safe zone guidelines.
- **Customizable Inputs:** Accepts a foreground image and background color as inputs to tailor the icon to your app’s branding.
- **Command Line Interface:** Easily run the script from the command line and integrate it into your development workflow.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/meapps/Expo-Adaptive-Icon-Generator.git
   cd Expo-Adaptive-Icon-Generator
   ```

2. **Set Up a Virtual Environment (Optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Python script from the command line. You can provide parameters such as the path to your foreground image and the background color.

### Command Line Example

```bash
python generate_icon.py --foreground ./assets/my-icon.png --background "#FFFFFF" --output ./output
```

**Parameters:**
- `--foreground`: Path to your foreground image (e.g., a PNG file with transparency).
- `--background`: Background color in HEX format to use for the icon.
- `--output`: Directory where the generated adaptive icon assets will be saved (defaults to the script’s output folder if not specified).

The script will generate the necessary image assets in various resolutions, according to Android’s adaptive icon guidelines.

## Configuration

If you prefer not to input options every time on the command line, you can modify the configuration within the script or use a configuration file (if supported). Key options include:
- **Foreground Image Path:** The path of your icon’s main image.
- **Background Color:** The HEX color used as a background.
- **Output Directory:** The location where the generated icons will be stored.
- **Icon Resolutions:** Predefined resolutions for MDPI, HDPI, XHDPI, XXHDPI, and XXXHDPI.

Refer to the inline comments in the Python script for details on how to adjust these parameters.

## Integration with Expo

Once your assets have been generated, update your Expo app configuration (typically in `app.json` or `app.config.js`) to use the new adaptive icon:

```json
{
  "expo": {
    "android": {
      "adaptiveIcon": {
        "foregroundImage": "./path/to/generated/foreground.png",
        "backgroundColor": "#FFFFFF"
      }
    }
  }
}
```

This configuration ensures that your Expo app will display a properly designed adaptive icon across all Android devices.

## Contributing

Contributions are welcome! If you have ideas for improvements, encounter any bugs, or want to add new features, please open an issue or submit a pull request. For contribution guidelines, please see [CONTRIBUTING.md](CONTRIBUTING.md) (if available).

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

