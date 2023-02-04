# Launches map from the browser using contents from the command line
import webbrowser, sys

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])

print(address)
webbrowser.open('https://www.google.com/maps/place/'+address)



