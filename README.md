# ClipboredLinkParser

ClipboredLinkParser is a Python script that automatically parses links and generates HTML anchor tags when you copy text to the clipboard. This tool can be particularly helpful when you are listing videos from platforms like YouTube, Facebook, or any other medium.

## How it works

The script utilizes the `pyperclip` library to monitor changes in the clipboard. Whenever a change is detected, it checks if the new clipboard data contains a link using regular expressions. If a link is found, it extracts the name and URL, creates an HTML anchor tag with the provided information, and appends it to an HTML file specified by the user.

## Getting Started

To use ClipboredLinkParser, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies 
3. Run the script by executing `python clipbored_link_parser.py` in your terminal.
4. Enter a file name when prompted to create an HTML file.
5. Start copying text containing links, and ClipboredLinkParser will automatically parse and save them as HTML anchor tags.

Feel free to modify the script according to your specific needs or integrate it into your own projects.

Enjoy parsing links with ease using ClipboredLinkParser!
