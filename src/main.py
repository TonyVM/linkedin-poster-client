import flet as ft
import requests


class LinkedInPostApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "LinkedIn Post Generator"
        self.page.window.width = 600
        self.page.window.height = 750  # Increased from 700 to 750
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # URL del webhook
        self.webhook_url = ft.TextField(
            label="Webhook URL",
            hint_text="https://hook.make.com/your-webhook-url",
            width=600,
            value="",
        )

        # Target language dropdown
        self.target_lang_dropdown = ft.Dropdown(
            label="Target Language",
            width=600,
            options=[
                ft.dropdown.Option("English"),
                ft.dropdown.Option("Spanish"),
                ft.dropdown.Option("French"),
                ft.dropdown.Option("German"),
                ft.dropdown.Option("Italian"),
                ft.dropdown.Option("Portuguese"),
                ft.dropdown.Option("Chinese"),
                ft.dropdown.Option("Japanese"),
                ft.dropdown.Option("Korean"),
                ft.dropdown.Option("Russian"),
                ft.dropdown.Option("Arabic"),
                ft.dropdown.Option("Hindi"),
                ft.dropdown.Option("Dutch"),
                ft.dropdown.Option("Swedish"),
                ft.dropdown.Option("Norwegian"),
            ],
            value="English",  # Default value
        )

        # Response area for URL tab
        self.url_response_area = ft.TextField(
            label="Result: ",
            multiline=False,
            read_only=True,
            width=300,  # Reduced width for horizontal layout
        )

        # Response area for Text tab
        self.text_response_area = ft.TextField(
            label="Result: ",
            multiline=False,
            read_only=True,
            width=300,  # Reduced width for horizontal layout
        )

        # Tabs para los diferentes tipos de entrada
        self.tabs = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(text="URL", icon=ft.Icons.LINK, content=self.create_url_tab()),
                ft.Tab(
                    text="Text",
                    icon=ft.Icons.TEXT_FIELDS,
                    content=self.create_text_tab(),
                ),
            ],
        )

        # Status
        self.status_text = ft.Text(value="Ready to send", color=ft.Colors.BLUE_600)

        self.build_ui()

    def create_url_tab(self):
        self.url_input = ft.TextField(
            label="URL to process",
            hint_text="https://example.com/article",
            width=500,
            multiline=False,
        )

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Enter the URL you want Make.com to process:", size=16),
                    self.url_input,
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                text="Send URL",
                                icon=ft.Icons.SEND,
                                on_click=lambda e: self.send_request(
                                    "url", self.url_input.value
                                ),
                            ),
                            ft.Container(width=20),  # Spacer
                            ft.Container(
                                content=self.url_response_area,
                                expand=True,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ],
                spacing=20,
            ),
            padding=20,
        )

    def create_text_tab(self):
        self.text_input = ft.TextField(
            label="Text/Idea for the post",
            hint_text="Write your idea or prompt to generate the post...",
            width=500,
            multiline=True,
            min_lines=3,
            max_lines=6,  # Reduced from 8 to 6
        )

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Enter the text or idea to generate the post:", size=16),
                    ft.Container(
                        content=self.text_input,
                        height=180,  # Fixed height to prevent overflow
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                text="Send Text",
                                icon=ft.Icons.SEND,
                                on_click=lambda e: self.send_request(
                                    "text", self.text_input.value
                                ),
                            ),
                            ft.Container(width=20),  # Spacer
                            ft.Container(
                                content=self.text_response_area,
                                expand=True,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ],
                spacing=20,
            ),
            padding=20,
        )

    def send_request(self, request_type: str, content: str):
        if not self.webhook_url.value.strip():
            self.show_error("Please enter the webhook URL")
            return

        if not content.strip():
            self.show_error("Please enter content to send")
            return

        if not self.target_lang_dropdown.value:
            self.show_error("Please select a target language")
            return

        try:
            # Clear previous status and results
            self.clear_previous_state(request_type)

            self.status_text.value = "Sending..."
            self.status_text.color = ft.Colors.ORANGE
            self.page.update()

            # Prepare data according to type
            data = {
                "type": request_type,
                "target-lang": self.target_lang_dropdown.value,
                "content": content,
            }

            # Make POST request
            response = requests.post(
                self.webhook_url.value.strip(),
                json=data,
                headers={"Content-Type": "application/json"},
                timeout=30,
            )

            # Show response
            if response.status_code == 200:
                self.show_success("Request sent successfully")
                status_code = response.status_code
                if request_type == "url":
                    self.url_response_area.value = f"Status Code: {status_code}"
                else:
                    self.text_response_area.value = f"Status Code: {status_code}"
            else:
                self.show_error("Request failed")
                status_code = response.status_code
                if request_type == "url":
                    self.url_response_area.value = f"Status Code: {status_code}"
                else:
                    self.text_response_area.value = f"Status Code: {status_code}"

        except requests.exceptions.Timeout:
            self.show_error("Timeout: The request took too long")
        except requests.exceptions.ConnectionError:
            self.show_error("Connection error: Check the webhook URL")
        except Exception as e:
            self.show_error(f"Unexpected error: {str(e)}")

        self.page.update()

    def clear_previous_state(self, request_type: str):
        """Clear previous status and result messages for a fresh start"""
        # Reset status to neutral state
        self.status_text.value = "Ready to send"
        self.status_text.color = ft.Colors.BLUE_600

        # Clear the appropriate result field
        if request_type == "url":
            self.url_response_area.value = ""
        else:
            self.text_response_area.value = ""

        # Update the UI immediately
        self.page.update()

    def show_success(self, message: str):
        self.status_text.value = message
        self.status_text.color = ft.Colors.GREEN

    def show_error(self, message: str):
        self.status_text.value = message
        self.status_text.color = ft.Colors.RED

    def build_ui(self):
        self.page.add(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(
                            "LinkedIn Post Generator",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_700,
                        ),
                        ft.Text(
                            "Send content to your Make.com flow to generate "
                            "LinkedIn posts",
                            size=14,
                            color=ft.Colors.GREY_700,
                        ),
                        ft.Divider(),
                        self.webhook_url,
                        self.target_lang_dropdown,
                        ft.Divider(),
                        self.tabs,
                        ft.Divider(),
                        self.status_text,
                    ],
                    spacing=20,
                ),
                padding=30,
            )
        )


def main(page: ft.Page):
    LinkedInPostApp(page)


def run_app():
    ft.app(target=main)


if __name__ == "__main__":
    run_app()
