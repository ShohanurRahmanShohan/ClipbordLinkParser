import pyperclip
import time
import re
# Prompt the user for a file name
filename = input("Enter a file name: ")

# Initialize the clipboard data
clipboard_data = pyperclip.paste()

# Define a function to check for clipboard changes
def check_clipboard():
    global clipboard_data
    while True:
        # Get the current clipboard data
        current_data = pyperclip.paste()

        # Check if the clipboard data has changed
        if current_data != clipboard_data:
            # Trigger the event handler
            on_clipboard_change(current_data)
            # Update the clipboard data
            clipboard_data = current_data

        # Wait for some time before checking again
        time.sleep(1)

# Define the event handler function
def on_clipboard_change(new_data):
    # Use regular expressions to find the link and name
    match = re.search("(?P<name>.*?):\s*(?P<url>https?://[^\s]+)", new_data)

    if match is not None:
        # Get the name and URL from the match object
        name = match.group("name")
        url = match.group("url")

        # Create an HTML anchor tag with the name and URL
        new_string = f'<a href="{url}"  target="_blank"  style="color: blue; text-decoration: underline;">{name}</a> <br>'

        # Save the new string to an HTML file
        with open(filename, 'a', encoding='utf-8') as f:
            f.write("%s\n" % new_string)
            print('Link is Created')



# Start the clipboard monitoring loop
check_clipboard()

