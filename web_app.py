#!/usr/bin/env python3
"""
LinkedIn Post Generator - Web Version
Runs the application in web browser mode
"""

import flet as ft
from src.main import main


def run_web_app():
    """Run the application in web browser mode"""
    ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,
        port=8088,
        host="0.0.0.0",  # Allow access from other devices on network
        web_renderer=ft.WebRenderer.HTML,
    )


if __name__ == "__main__":
    print("🚀 LinkedIn Post Generator - Web Version")
    print("📱 Opening in web browser...")
    print("🌐 Access at: http://localhost:8088")
    print("🔗 Or from other devices: http://[your-ip]:8088")
    print("⌨️  Press Ctrl+C to stop")
    run_web_app()
