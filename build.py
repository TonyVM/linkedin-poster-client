#!/usr/bin/env python3
"""
Build scripts for LinkedIn Post Generator
Compile the application for different platforms
"""

import subprocess
import sys
import os


def build_android_apk():
    """Build Android APK"""
    print("🤖 Building Android APK...")
    cmd = [
        "flet",
        "build",
        "apk",
        "--project",
        "linkedin-poster-client",
        "--description",
        "Client app to send content to Make.com workflows for LinkedIn post generation",
        "--org",
        "com.tonyvm",
        "--product",
        "LinkedIn Post Generator",
        "--build-version",
        "0.1.0",
        "--build-number",
        "1",
        "--company",
        "Antonio Valladares",
        "--copyright",
        "Copyright 2024 Antonio Valladares",
    ]

    try:
        subprocess.run(cmd, check=True)
        print("✅ Android APK built successfully!")
        print("📱 APK location: ./build/apk/")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error building Android APK: {e}")
        sys.exit(1)


def build_android_aab():
    """Build Android App Bundle (AAB) for Play Store"""
    print("🤖 Building Android AAB for Play Store...")
    cmd = [
        "flet",
        "build",
        "aab",
        "--project",
        "linkedin-poster-client",
        "--description",
        "Client app to send content to Make.com workflows for LinkedIn post generation",
        "--org",
        "com.tonyvm",
        "--product",
        "LinkedIn Post Generator",
        "--build-version",
        "0.1.0",
        "--build-number",
        "1",
        "--company",
        "Antonio Valladares",
        "--copyright",
        "Copyright 2024 Antonio Valladares",
    ]

    try:
        subprocess.run(cmd, check=True)
        print("✅ Android AAB built successfully!")
        print("📱 AAB location: ./build/aab/")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error building Android AAB: {e}")
        sys.exit(1)


def build_web():
    """Build Web application"""
    print("🌐 Building Web application...")
    cmd = [
        "flet",
        "build",
        "web",
        "--project",
        "linkedin-poster-client",
        "--description",
        "Client app to send content to Make.com workflows for LinkedIn post generation",
        "--product",
        "LinkedIn Post Generator",
        "--base-url",
        "/",
        "--web-renderer",
        "html",
    ]

    try:
        subprocess.run(cmd, check=True)
        print("✅ Web application built successfully!")
        print("🌐 Web files location: ./build/web/")
        print("📄 Deploy the contents of build/web/ to your web server")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error building Web application: {e}")
        sys.exit(1)


def show_help():
    """Show available build options"""
    print(
        """
🔨 LinkedIn Post Generator - Build Script

Available commands:
  android     Build Android APK
  aab         Build Android App Bundle (for Play Store)
  web         Build Web application
  help        Show this help message

Usage:
  python build.py <command>

Examples:
  python build.py android
  python build.py aab
  python build.py web
"""
    )


def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    if command == "android" or command == "apk":
        build_android_apk()
    elif command == "aab":
        build_android_aab()
    elif command == "web":
        build_web()
    elif command == "help" or command == "--help" or command == "-h":
        show_help()
    else:
        print(f"❌ Unknown command: {command}")
        show_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
