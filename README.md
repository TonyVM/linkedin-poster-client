# LinkedIn Post Generator

A simple desktop application built with Flet that allows you to send content to Make.com webhooks for automatic LinkedIn post generation.

## Features

- **URL Processing**: Send URLs to extract and process content for LinkedIn posts
- **Text/Idea Processing**: Submit text ideas or prompts to generate LinkedIn posts
- **Document Processing**: Upload documents (TXT, PDF, DOCX, MD) for content analysis and post generation
- **Status Feedback**: Real-time status updates and HTTP response codes
- **Clean UI**: Modern, tab-based interface built with Flet

## Project Structure

```
├── README.md
├── pyproject.toml
└── src
    ├── assets
    │   └── icon.png
    └── main.py
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/linkedin-post-generator.git
cd linkedin-post-generator
```

2. Install dependencies using uv:
```bash
uv pip install -r requirements.txt
```

Or install the project in development mode:
```bash
uv pip install -e .
```

## Usage

1. Run the application:
```bash
python src/main.py
```

2. Enter your Make.com webhook URL in the top field

3. Choose your content type:
   - **URL Tab**: Enter a URL you want to process
   - **Text Tab**: Write your idea or prompt
   - **Document Tab**: Select a document file to upload

4. Click the corresponding "Send" button

5. Check the status and result code in the response field

## Configuration

Make sure your Make.com webhook is configured to accept:
- POST requests with JSON data for URL and text types
- Multipart form data for document uploads

### Expected Data Formats

**URL/Text requests:**
```json
{
    "type": "url|text",
    "url": "https://example.com" // or
    "text": "Your content here"
}
```

**Document requests:**
```
POST /webhook
Content-Type: multipart/form-data

type=document
document=[file data]
```

## Dependencies

- **Flet**: Modern UI framework for Python
- **Requests**: HTTP library for webhook communication

## Development

The application is built with Python and uses:
- Flet for the GUI
- Requests for HTTP communication
- Modern Python packaging with pyproject.toml

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
