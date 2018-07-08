# Project 3 - Country Quiz with Flask

### What does it do and what need does it fulfil?

This project uses skills learnt to build a mobile-first responsive Website that uses the Flask framework to build a Country Quiz.  The Website can be found at [http://cquiz-env.dmvjfcwwp2.eu-west-1.elasticbeanstalk.com/] 

### Functionality of project

The website is fully responsive, and uses a text file to hold a user list and score (if they complete the quiz) as well as a JSON file which holds the questions and links to the picture for each country.

The first page has a input box which the user adds their name which must be a non-empty, unique, single name. This is validated, if it fails it returns a message to the user. Upon a unique name being inputted the program writes it to the text file. 

The question page extension is generated by using the unique single name. It works by reading the JSON file which holds the question number, country picture URL and its name. There is an input box that the user enters the country. The user gets 3 guesses and can score upto 3 points for each question. If the user gets the question wrong then the question is worth 2 points and so on. After 3 wrong guesses Inspector Flask remembers the country and the quiz moves on a question. Validation checks are done to ensure the user enters something, whether it is correct or not and whether the user has already guessed that answer.  Javascript and jQuery is used for this and when a wrong or correct input is submitted fadeOut() is used to deliver 'wrong' or 'correct'. Each wrong answer is added to a list to help the user remember what he has guessed before. After ten questions it saves the score next to the relevant line on the users text file and moves onto the high score page. 

The high score page reads in the users text file and adds each user with a score onto a table, it then reverse orders this table on score and displays it on page.

### Technologies Used

- HTML5
- CSS3
- Bootstrap
- Python
- Flask
- Javascript and JQuery
- Bash
- Ubuntu
- GIT
- GITHUB
- Docker
- AWS Elastic Beanstalk (EC2 + Docker Recipe)
- Google Chrome developer tools
- PyCharm IDE

### Deployment

Website was coded in PyCharm IDE, a local GIT directory was used for version control and then uploaded to GITHUB. I then researched AWS and Docker, this was due to having recently found employment as a developer with some sys admin responsibilities. So I installed Docker on my local machine as well as Amazon's AWS EB CLI (Elastic beanstalk command line interface) and wrote a Dockerfile. I used this to then build the Docker image, calling it country-quiz:0.1 (for version control in docker) and tagged that as the latest. I then pushed the latest image to the Docker volume on my AWS server. I was able to do all this within the free tier AWS offers. 

Each update I made to the website I uploaded it to Github, built a docker image incrementing the version number (0.1, 0.2, 0.3 etc.); then I taged this image as the latest and pushed it to server thus:

1. git status
2. git add .
3. git commit -m 'the message'
4. git push -u origin master
5. dockerbuild -t countryQuiz:1.0 .
6. docker tag countryquiz:1.0 5pence/countryquiz:latest
7. docker push 5pence/countryquiz:latest

Then I went to my AWS server dashboard and clicked 'rebuild the server'. 

### Testing

Each page was tested locally and online (the AWS server) using Chrome developer tools, testing its functionality as well as look and feel (in landscape and portrait mode) on Galaxy S5, Nexus 5S, Nexus 6P, iPhone 7, iPhone 7 Plus, iPhone 8, iPhone 8 Plus, iPhone X, iPad, iPad Pro and responsive desktop.

All input boxes where checked for validation:
- empty strings
- names for more than one word
- unique name
- country names repeated for the same question

In order to deal with letter cases I have converted all names into lowercase and all countries into capitals, this then helped making checks easier. All inputs I also trimmed for extra whitespaces.

I also checked the names form when building the high score table, I found an error if a user started but didn't finish their quiz (though either giving up or using the quiz concurrently). The method was crashing as it was trying to read lines that had no score. So a simple line 'if len(line.split()) > 1:' statement resolves this when building the table, that way it ignores the lines that have just a name only. I then tried a number of different methods to order the table but researched lambda functions and used 'score_table.sort(key=lambda s: s[1], reverse=True)'. I now find lambdas and other functional programming techniques to be most useful. 


### What changed after user design experience (UDX) phase

I had planned to use a users.txt file as well as a highscore.txt file, however as I coded it I realised it would be better modelled by adding their scores next to their name and building the high score table from that. This would save having to have an extra text file and also save file i/o transactions.
 