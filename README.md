# Recipe Share

### [View the live page here](https://recipe-share-58fcaea24fd7.herokuapp.com/)



![Responsive](./assets/docs/am-i-responsive.png)

## How to play



## User Experience



### Color Palette



### User Stories

#### As a first time visitor I want to:



#### As a returning visitor I want to:



#### As a frequent visitor I want to:



## Features



### Existing Features

- Main screen

    ![Logo](./assets/docs/logo-welcome.png)

    ![Rules](./assets/docs/rules.png)

    ![Rules error](./assets/docs/rules-error.png)

- Game display:

    ![Game display](./assets/docs/game-display.png)

- Correct guess:

    ![Correct](./assets/docs/correct.png)

- Incorrect guess:

    ![Incorrect](./assets/docs/incorrect.png)

- Errors on guess:

    ![Not a letter](./assets/docs/not-letter.png)

    ![More than one letter](./assets/docs/one-letter.png)

    - This updates as the user guesses a new letter:

    ![Guessed letters](./assets/docs/guessed-letters.png)

- Play again:

    ![Play again](./assets/docs/play-again.png)

### Future Features



## Flowchart

![Flowchart](./assets/docs/flowchart.png)

## Testing

### CI Python Linter

Functions were tested using [CI Python linter](https://pep8ci.herokuapp.com/) throughout the building process, making the final testing stage simpler and a smoother process.
![run.py](./assets/docs/run.png)
![words.py](./assets/docs/word-list.png)
![hangman_stage.py](./assets/docs/hangman.png)

### Manual Testing

|What was tested|Result|
|---|---|
||Passed|
||Passed|
||Passed|
||Passed|
||Passed|
||Passed|
||Passed|
||Passed|

### Fixed bugs

|What was tested / Expected results|Actual Results|What was done to fix the bug|
|---|---|---|
||||
||||
||||

## Deployment

### [Heroku](https://heroku.com/apps) deployment

1. Login to Heroku
2. On the Heroku dashboard click on 'New'
3. Select 'Create New App'
4. Add an app name and select your region
5. Click 'Create App'
6. On the next page at the top click 'Settings' then 'Config Vars'
7. Click 'Reveal Config Vars' then add 'Port' key and value '8000' (Optional)
8. Scroll down and click 'Buildpack'
9. 'Add', 'Python' & 'Node.js' with Python being first (above) Node.js
10. At the top of the page again, click 'Deploy'
11. Click on 'Github' as your deployment method
12. Search the relevant repo and link these
13. Once linked, select 'Automatic deploys from' or 'Manual Deploy'
14. The app will now be hosted on Heroku.

### Cloning the GitHub repository

Cloning a repository will download a full copy of the data to your computer. This is useful when larger commits need to be pushed, adding or removing files and fixing merge conflicts.

1. Login to GitHub
2. Click the repository you wish to clone (Top left corner)
3. Click 'Code' which is shown above the list of files in the repository
4. Click the 'Local' tab, copy the HTTPS URL
5. Open Codeanywhere, click 'New Workspace'
6. Paste the copied URL into the space given under 'Repository URL'
7. Click 'Create' and the local clone will be created.

### Forking the GitHub repository

Forking a GitHub repository will allow you to make a copy of the repository, changes can then be made that will not affect the original repository. This is useful for proposed changes, ideas, fixes to an original repository.

1. Login to GitHub
2. Click the repository you wish to fork (Top left corner)
3. Click the 'Fork' drop-down in the top right-hand corner
4. Then click 'Create a new fork' you will now have a copy to work on.

## Technologies, Libraries, Frameworks & Programs Used

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    - Python was used to structure the content of the app
- [GitHub](https://github.com/)
    - GitHub is being used to store the code for this web page
- [Gitpod](https://gitpod.io/)
    - Gitpod was used as the development environment for this web page
- [CI Python Linter](https://pep8ci.herokuapp.com/)
    - Used to validate the code and functions
- [Heroku](https://heroku.com/apps)
    - Used to deploy the app
- [Am I Responsive?](https://ui.dev/amiresponsive)
    - Used to for the image in the README file
- [DB Diagram](https://dbdiagram.io/)
    - Used to for the image in the README file

## Credits

- Slack community for guidance:
  - [Slack Community](https://app.slack.com/client/T0L30B202/C027C3PLS1W)

## Acknowledgements

Thank you to my mentor Mitko Bachvarov for his guidance, advice, support as well as my husband and fellow student Iain Jackson for his advice, motivation, troubleshooting assistance throughout the process of this project.