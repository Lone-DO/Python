import data
from Display import Display

Leave = ["q", "quit", "exit", "terminate", "close"]
reddit = data.client()

# reddit.fetch()

while True:
    print("""Welcome to the Reddit Console Client
    Enter --help for list of options
    Enjoy
    """)
    userInput = input("\t")
    if (userInput.lower() in Leave): break
    if (userInput.lower() == "load"): 
        # reddit.fetch()
        Display(reddit.data)
print("Goodbye")