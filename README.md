# AutoCookieBot

## Overview
AutoCookieBot is a Python script using Selenium to automate the clicking and purchasing process in the "Cookie Clicker" web game. It clicks on the cookie to accumulate points and purchase items from the store to optimize the gameplay.

## Prerequisite
  Python installed

  Chrome browser installed

  ChromeDriver installed (compatible with your Chrome version)

## Installation
  Clone the repository -> git clone https://github.com/mohamedsanoko/Cookie-Clicker.git

  Install the required Python packages -> pip install selenium

  Download the appropriate ChromeDriver version from https://sites.google.com/chromium.org/driver/ and place it in the project directory

## Usage
  1. Run the script: python main.py

  2. The script will open a Chrome browser, navigate to the "Cookie Clicker" game, and start clicking the cookie.

  3. Every 5 seconds, it will check the available money and purchase the most expensive item from teh store that can be afforded.

  4. The script runs for a default duration of 5 minutes.

  5. The cookies per second (cps) will be displayed at the end of the execution

## Customization
You can modify the 'multiplication_factor' to change the duration of the process.

Ensure that the XPATH expressions used for locating elements are still valid, as they may change with updates to the game's website.
