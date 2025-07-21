#!/usr/bin/env python3
"""
LinkedIn Post Generator - Android Build Entry Point
This file is used for mobile app builds (Android/iOS)
"""

from src.main import main

if __name__ == "__main__":
    import flet as ft

    ft.app(target=main)
