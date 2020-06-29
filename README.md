# Python - Reddit Console Client (RCC)
Code Louisville Project, Python, May 2020 

# How to use
 - Clone project
 - Be sure to install any missing dependencies
 - In the Console, run
 ```
   python main
 ```
 - This is a Python Console Application, Enjoy
 - Input --help for a list of instructions/ options
 ```
 --help
 
 #returns the following
 The following commands are available,
    "help", "-help", "--help", "-h", "--h" to list options
    "Load", [optional args: 'prev', 'next']
    "List", [optional args: 'array/ post #]
    "Settings", to browse settings/ current parameters
    "Change" (setting), [arg: "Channel", "Sort", "time", "region"]
    "Refresh", to reload content (call after changing a setting)
    "Reset", restarts application with default settings
 ```
 
## Create Reddit Console Client App - Browse Reddit (Text Only)

Simple consolse interface for browsing reddit, utilizing the same Reddit UI Hierarchy

## CRITERIA SELECTED FROM @CodeLouisville [WIKI](https://github.com/CodeLouisville/Student-Resources/wiki/Project-Requirements)

- Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
   > [main.py](https://github.com/Lone-DO/Python/blob/master/main.py) => Client will run until user input is a exit statement
   ```python
   main.py
   ...
   if args[0] in ["q", "quit", "exit", "terminate", "close"]:
        break
   ...
   ```
- Create a class, then create at least one object of that class and populate it with data
   > [Data.py](https://github.com/Lone-DO/Python/blob/master/data.py) => 'Client' Class for maintaing state, another static class 'Display' for controlling calls
- Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
   > [Display.py](https://github.com/Lone-DO/Python/blob/master/Display.py), Filtered data from API is stored for rendering later in the UI
   ```
   Display.list, Display.data, Display.loop() => items[]
   ```
- Read data from an external file, such as text, JSON, CSV, etc and use that data in your application
   > [mockdata.json](https://github.com/Lone-DO/Python/blob/master/mockdata.json) => for testing, Api JSON for live use
- Create and call at least 3 functions, at least one of which must return a value that is used
   > State management, OOP, list of commands for browsing client
- Connect to an external/3rd party API and read data into your app
   > [Data.py](https://github.com/Lone-DO/Python/blob/master/data.py) => [Reddit Api](https://www.reddit.com/r/popular.json) changes based on user settings
- Calculate and display data based on an external factor (ex: get the current date, and display how many days remaining until some event)
   > [ConvertTime.py](https://github.com/Lone-DO/Python/blob/master/ConvertTime.py) => Converting Api UTC data to "posted since ... \", Ex. posted 10 days ago/ 3 hours ago,

## Order of Operations

### Pull Data From Reddit Api

-  [x] Create Method for handling calls
   -  [x] Default method to GET Articles from initial Subreddit
      -  [x] Sort method to sort Articles based on user selection...
         > ["hot","new","rising","top"]
      -  [x] Load method to GET more Articles via last child's ID...
         ```python
            main.py
            ...
            # Return child via num/index
            def getChild(num): return data[num].get("data")["name"]
            ...
            reddit.setAfter(getChild(len(data) - 1))
            ...
         ```
-  [ ] Create Method to GET Article Comments

### Render data from Api

-  [x] Create Model
-  [x] Loop Data and replicate Model
   -  [x] Filter Data...
   ```python
   ...
   for index, child in tqdm(enumerate(data, 0), total=len(data)):
      data = child.get("data")
      Name = data.get("name")  # Pass Last child to Pages Array
      Title = data.get("title")
      Author = data.get("author")
      Link = data.get("permalink")
      Created = data.get("created")
      Score = data.get("score")
      numComments = data.get("num_comments")
      Domain = data.get("domain")
      Prefix = data.get("subreddit_name_prefixed")
      Name = data.get("name")
      Title = data.get("title")
      Text = data.get("selftext")
   ...
   ```
   -  [x] Call Model...
   -  [x] Set generated item to list items[]
   -  [x] Render body to console UI
      ```python
      print(f"""
        [{index}] {Title} ({Domain})
        submitted {ConvertTime(Created)} by u/{Author} to {Prefix}
        {Score} upvotes with {self.CommentCount(numComments)} comments
        Link: {Link}
      """)
      ```

### Add Event handlers
-  [x] If no Argument is passed, show relative options
-  [x] Method for modyfing settings
    -  [x] Method for handling errors
    -  [x] Change Sort [arg]
    -  [x] Change Channel [arg]
    -  [x] Change Time [arg]
    -  [x] Change Region [arg]

### Add Some whitespace for readability \(Keep It Simple)

### :shipit: Ship App

> Due Date: July 31, 2020 (12pm EST)
