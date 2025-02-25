# Focusing - Minimalistic Stopwatch for Windows

![Focusing Timer Screenshot](https://github.com/user-attachments/assets/bc8689e6-7eb9-4b13-9997-82079e33406b)

A simple, minimalistic, and lightweight stopwatch application for Windows that stays out of your way while helping you stay focused.

## Features

- **Ultra-Minimal Design**: Dark theme with clean interface
- **Always on Top**: Pin the timer to keep it visible over other applications
- **Lightweight**: Uses minimal system resources
- **Draggable**: Position it anywhere on your screen
- **Distraction-Free**: No unnecessary features or distractions

## Controls

The application has just three buttons:

- **Start/Pause** - Begin or pause the stopwatch
- **Stop** - Reset the timer back to 00:00:00
- **Pin** - Toggle always-on-top functionality

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Method 1: Running from Source

1. Clone this repository:
   ```
   git clone https://github.com/EugeneLiutko/SimpleMinimalisticStopwatch.git
   cd Focusing-MinimalisticStopwatch
   ```

2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python stopwatch.py
   ```

### Method 2: Building Executable

1. Clone the repository and install dependencies as shown above

2. Build standalone executable:
   ```
   pyinstaller --onefile --windowed --icon=clock.ico stopwatch.py --name Focusing
   ```

3. Find the executable in the `dist` folder

## Requirements

Dependencies are listed in `requirements.txt`:
- PyQt6

## Usage

- **Moving the Stopwatch**: Click and drag anywhere on the stopwatch to reposition it
- **Starting/Stopping**: Use the respective buttons to control the stopwatch
- **Keep on Top**: Pin the stopwatch to keep it visible above all other windows
- **Closing**: To exit the application, right-click on it in the taskbar and select Close

## Why Use Focusing?

Unlike complex productivity apps with numerous features, Focusing is designed to do just one thing well - track time. Its minimal footprint and distraction-free design help you concentrate on your work, not on your tools.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Made with ❤️ for productivity enthusiasts who value simplicity.
