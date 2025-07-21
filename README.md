# LinkedIn Post Generator

A cross-platform application built with Flet that allows you to send content to Make.com webhooks for automatic LinkedIn post generation with multi-language support. Runs on Desktop (Windows, macOS, Linux), Web, and Mobile (iOS, Android).

## Features

- **Cross-platform Support**: Runs on Desktop (Windows, macOS, Linux), Web browsers, and Mobile devices (iOS, Android)
- **URL Processing**: Send URLs to extract and process content for LinkedIn posts
- **Text/Idea Processing**: Submit text ideas or prompts to generate LinkedIn posts
- **Multi-language Support**: Generate posts in 15 different languages (English, Spanish, French, German, Italian, Portuguese, Chinese, Japanese, Korean, Russian, Arabic, Hindi, Dutch, Swedish, Norwegian)
- **Real-time Status Feedback**: Live status updates with color-coded messages and HTTP response codes
- **Modern UI**: Clean, tab-based interface with horizontal layout optimization
- **Error Handling**: Comprehensive error management for network issues and invalid inputs

## Platform Support

This application supports multiple platforms thanks to Flet's cross-platform capabilities:

### Desktop
- **Windows**: Native Windows application
- **macOS**: Native macOS application  
- **Linux**: Native Linux application

### Web
- **Browser**: Runs in any modern web browser
- **Progressive Web App (PWA)**: Can be installed as a web app

### Mobile
- **Android**: Native Android application
- **iOS**: Native iOS application

All platforms share the same codebase and user interface, ensuring consistent functionality across devices.

## Screenshots

The application features a clean, intuitive interface with:
- Webhook URL configuration
- Target language selection dropdown
- Two main processing modes (URL and Text)
- Side-by-side Send button and Result display
- Real-time status indicators

## Project Structure

```
linkedin-post-generator/
├── .gitignore
├── README.md
├── pyproject.toml
├── requirements.txt
└── src/
    ├── assets/
    │   └── icon_placeholder.txt
    └── main.py
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip or uv package manager

### Setup

1. Clone this repository:
```bash
git clone https://github.com/tonyvm/linkedin-poster-client.git
cd linkedin-poster-client
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies using uv (recommended):
```bash
uv pip install -r requirements.txt
```

Or using pip:
```bash
pip install -r requirements.txt
```

Alternatively, install in development mode:
```bash
uv pip install -e .
```

## Usage

### Running the Application

#### Desktop Application (Default)

1. Start the desktop application:
```bash
python src/main.py
```

2. The application window will open (600x750 pixels) with the LinkedIn Post Generator interface.

#### Web Application

1. Run as a web application:
```bash
python -c "import flet as ft; from src.main import main; ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080)"
```

2. Open your browser and navigate to `http://localhost:8080`

#### Mobile Development

For mobile deployment, you'll need to:

1. **Android**: Use Flet's Android packaging tools
2. **iOS**: Use Flet's iOS packaging tools

Refer to [Flet documentation](https://flet.dev/docs/guides/python/packaging-app-for-distribution) for detailed mobile packaging instructions.

### Using the Application

1. **Configure Webhook URL**: Enter your Make.com webhook URL in the top field
   - Example: `https://hook.make.com/your-webhook-id`

2. **Select Target Language**: Choose from 15 available languages in the dropdown menu

3. **Choose Content Type**:
   - **URL Tab**: Enter a URL you want Make.com to process and extract content from
   - **Text Tab**: Write your idea, prompt, or content directly

4. **Send Request**: Click the "Send URL" or "Send Text" button

5. **Monitor Results**: 
   - Status messages appear at the bottom (Ready/Sending/Success/Error)
   - HTTP response codes are displayed next to the send button
   - Color-coded status indicators (Blue=Ready, Orange=Processing, Green=Success, Red=Error)

## API Integration

### Make.com Webhook Configuration

Your Make.com webhook should be configured to accept POST requests with the following JSON structure:

```json
{
    "type": "url",
    "target-lang": "English",
    "content": "https://example.com/article"
}
```

Or for text content:

```json
{
    "type": "text",
    "target-lang": "Spanish",
    "content": "Generate a LinkedIn post about AI trends in 2024"
}
```

### Response Handling

The application expects:
- **Success**: HTTP 200 status code
- **Error**: Any other status code will be treated as an error
- **Timeout**: 30-second timeout for requests

## Technical Details

### Dependencies

- **Flet ≥0.28.0**: Cross-platform GUI framework for Python (Desktop, Web, Mobile)
- **Requests ≥2.25.0**: HTTP library for API communication

### Architecture

- **Main Class**: `LinkedInPostApp` - Handles UI and business logic
- **UI Components**: Tab-based interface with responsive layout
- **Error Handling**: Comprehensive exception management for network issues
- **State Management**: Clear previous state mechanism for fresh requests

### Key Features Implementation

- **Cross-platform Compatibility**: Single codebase runs on desktop, web, and mobile
- **Responsive Design**: Adapts to different screen sizes and orientations
- **Horizontal Layout**: Send buttons and result fields are positioned side-by-side
- **Auto-clearing**: Previous status and results are automatically cleared on new requests
- **Language Selection**: 15 pre-configured language options
- **Input Validation**: Validates webhook URL, content, and language selection
- **Responsive Design**: Fixed window size with optimized component spacing

## Development

### Building from Source

The project uses modern Python packaging with `pyproject.toml`:

```bash
# Install in development mode
uv pip install -e .

# Run as desktop application
python -m src.main

# Run as web application
python -c "import flet as ft; from src.main import main; ft.app(target=main, view=ft.AppView.WEB_BROWSER)"

# Or use the console script
linkedin-post-generator
```

### Mobile App Packaging

For mobile app distribution:

```bash
# Android APK
flet pack src/main.py --platform android

# iOS IPA (requires macOS and Xcode)
flet pack src/main.py --platform ios
```

### Web App Deployment

For web deployment:

```bash
# Build for web
flet pack src/main.py --platform web

# Deploy to web server
# Upload the generated web files to your web server
```

### Project Metadata

- **Author**: Antonio Valladares
- **License**: MIT License
- **Python Version**: ≥3.8
- **Platforms**: Windows, macOS, Linux, Web, Android, iOS
- **Repository**: https://github.com/tonyvm/linkedin-poster-client

## Troubleshooting

### Common Issues

1. **Connection Error**: Check your internet connection and webhook URL
2. **Timeout Error**: The request took longer than 30 seconds
3. **Invalid Webhook URL**: Ensure the URL is properly formatted and accessible
4. **Empty Content**: Make sure to enter content in the URL or text field

### Error Messages

- **Blue Status**: Ready to send
- **Orange Status**: Request in progress
- **Green Status**: Request completed successfully
- **Red Status**: Error occurred (check the message for details)

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
