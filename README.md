# Virtual Painting with OpenCV and Mediapipe

This project is a computer vision-based virtual painting tool built using OpenCV and Mediapipe. It allows users to draw on the screen in real-time by detecting hand gestures using a webcam. The project features different colors, along with an eraser tool to clear parts of the drawing.

## Features

- **Hand Detection**: Utilizes Mediapipe's hand-tracking module to detect and track hands in real-time.
- **Drawing Mode**: Draw on the screen by making specific hand gestures. The drawing color and thickness can be customized.
- **Selection Mode**: Switch between different colors and the eraser tool by selecting options from the top of the screen.
- **Eraser Mode**: Erase parts of the drawing with a thicker brush size.
- **Real-time Drawing**: Draw and see your output instantly on the screen using the webcam feed.

## How It Works

- **Hand Detection**: The program uses Mediapipe to detect hand landmarks and track fingers.
- **Gesture Recognition**: Specific hand gestures are recognized to switch between selection and drawing modes.
  - **Two fingers up**: Enter selection mode to choose a drawing color or the eraser.
  - **Index finger up only**: Enter drawing mode and start drawing on the screen.
- **Canvas**: A virtual canvas is created where the drawing takes place. The drawing is updated in real-time as the hand moves.


## Usage
- **Color Selection**: Use the selection mode (two fingers up) to choose between different colors. Each color option is displayed at the top of the screen.
- **Drawing**: In drawing mode (index finger up), move your finger to draw on the canvas.
- **Eraser**: Select the eraser from the toolbar and use it to clear parts of the canvas.

## Dependencies
- **Python 3.x**
- **OpenCV**
- **Mediapipe**
- **Numpy**

![Screenshot 2024-08-18 090109](https://github.com/user-attachments/assets/9cb1b21b-633e-497e-b9c4-f82adfe63be7)

