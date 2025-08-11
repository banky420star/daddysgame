#!/bin/bash

# Car Racing Game Launcher
echo "🚗 Starting Car Racing Game..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.6+ first."
    exit 1
fi

# Check if pygame is installed
if ! python3 -c "import pygame" &> /dev/null; then
    echo "📦 Installing required dependencies..."
    pip3 install -r requirements.txt
fi

# Run the game
echo "🎮 Launching game..."
python3 car_racing_game.py 