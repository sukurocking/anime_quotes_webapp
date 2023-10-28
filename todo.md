- We will build an application, which will randomly display quotes from One Piece characters
- Store a collection of quotes from One Piece characters into a sqlite database
- The main page will consist of a button to randomly generate a quote
- On clicking the button, it will pull from the quotes' collection and display it on the main screen
- There will be a user interface for adding quotes as well. The form will consist of character name and the quote
    -  Dedupe by trimming the quote and display if the quote requested to be added is a duplicate. 
    -  The duplicate quote would not be added into the database



- [x] Create a database (and schema) consisting of quotes and characters
    - [x] The database should consist of a UNIQUE constraint for quote column
- [x] Create a Flask route for index page, Add a button to the index page, mentioning "Generate an Anime Quote!"
- [x] Create a Flask route for the random quote function, which is triggered on POST method (upon clicking on the button in the page)
- [x] Once the button is clicked, The POST method will display the random quote on the redirected page
- [ ] Add page for adding quote from frontend
- [ ] Allow functionality for searching quotes by character