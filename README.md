# Milestone Project 3

---

<p id="top"></p>

## Buy & Sell Marketplace

This project is a summary of study from the eight, ninth and tenth modules of the Full Stack Developer Course - Python Fundamentals, Practical Python and Data Centric Development, to create a fully Mobile Responsive CRUD Web Application.

Buy & Sell app is an online marketplace where users can buy and sell items. Purpose of this project is to create simple app where users can add new ads, browse and search for items and update or delete ads they added.

## Table of contents

- <a href="#project">Project Construction 👷</a>
- <a href="#ux">User Experience Design 🧠</a>
    - <a href="#us">User Stories</a>
    - <a href="#us">Design</a>
- <a href="#tech">Technologies Used 🔨</a>
  - <a href="#lang">Languages</a>
  - <a href="#flp">Frameworks, Libraries & Programs</a>
- <a href="#features">Features List 😲</a>
  - <a href="#existing">Existing Features</a>
  - <a href="#future">Future Features</a>
- <a href="#testing">Testing 🔥</a>
  - <a href="#manualtesting">Manual Testing</a>
  - <a href="#ustesting">User Stories</a>
  - <a href="#bugs">Bugs</a>
- <a href="#deployment">Deployment 🚀</a>
- <a href="#credits">Credits 🙏</a>
  - <a href="#code">Code</a>
  - <a href="#media">Media</a>
  - <a href="#ack">Acknowledgments</a>

<p id="project"></p>

## 1️⃣ Project Construction 👷

This application contains the key CRUD requirement functionality and utilises a data handling document based database, MongoDB. Functionality is created using Flask, HTML5, CSS and JavaScript. Materialize framework was used in building fronted structure to make sure app is responsive as possible and can be used on multiple screen sizes.

Application offer a registration and login system with password hashing to protect each user. Logged user can browse ads created by other registered users and create, update and delete ads created by him.

Un-registered users can also use the application, but their permissions are limited to viewing ads created by registered users only.

<div align="center"><p style="text-align: center"><a href="#top">Back to top ⬆️</a></p></div>

<p id="ux"></p>

## 2️⃣ User Experience Design 🧠

<p id="us"></p>

### User stories:

#### Guest (un-registered) User:

1. As a Guest user, I want to browse the ads added by registered users.
- All users can browse ads by selecting ad category or by search option on welcome page.
2. As a Guest user, I want to be able to see seller contact details or add my ads.
- For more permissions Guest can register using quick registration form and then login .
3. As a Guest user, I want app to be visually appealing and easy in use.
- Application is very intuitive to use and has clear layout.
4. As a Guest user,  I want to contact someone in the event something is wrong with the app.
- Contact information can be found in footer.

#### Registered User:

1. As a Registered User, I want to 'Log In' to my profile.
- Registered User can Log In using registered username and password.
2. As a Registered User, I want to add my ads.
- Registered User can start adding ad by clicking 'Place Ad' button in navigation bar.
3. As a Registered User, I want to Edit or Delete my ads.
- Edit and Delete buttons are placed in ad view page and are visible for advertiser.
4. As a Registered user, I want 'Profile' page where I can see my all ads.
-  Registered user will see 'Profile' tab in navigation after Log In.
5. As a Registered user, I want report ad when item is suspicious or not appropriate.
- Registered used can use 'Report Ad' button under ad.
5. As a Registered user, I want to 'Log Out'.

### Moderators

1. As Moderator, I want to delete or update any ad.
- Moderator can see Edit and Delete buttons for all ads.
2. As, Admin I want to see ad reports.
- Moderator can see all reports in table under ad.

### Admin:

1. As Admin, I want to ad new 'Categories'
- Admin have dedicated page where he can click 'Add Category' button.
2. As Admin, I want to delete or update any ad.
- Admin can see Edit and Delete buttons for all ads.
3. As, Admin I want to remove 'Registered User'.
- Admin have dedicated page where he can delete any user.
4. As, Admin I want to see ad reports.
- Admin can see all reports in table under ad.
5. As Admin I want to edit users permissions.
- Admin can create moderators and other admins.

### Developer:

1. As a Developer, I want to create database application app using Python and Flask.
2. As a developer, I want to create fully responsive app.
- Application is fully responsive thanks to Materialize framework.

<p id="design"></p>

### Design:

#### Color Scheme:

????????????????????????????????????????????????????????????????????

#### Typography:

????????????????????????????????????????????????????????????????????

#### Content Structure:

????????????????????????????????????????????????????????????????????????

#### Images:

??????????????????????????????????????????????????????????????????????????

#### Wireframes:

- <a href="static/readmeimages/desktop-wireframes.pdf" target="_blank">Desktop wireframes</a>
- <a href="static/readmeimages/mobile-wireframes.pdf" target="_blank">Mobile wireframes</a>

<div align="center"><p style="text-align: center"><a href="#top">Back to top ⬆️</a></p></div>

<p id="tech"></p>

## 3️⃣ Technologies Used 🔨

<p id="lang"></p>

### Languages Used:

- <a href="https://en.wikipedia.org/wiki/HTML" rel="noopener" target="_blank">HTML</a> - Standard mark-up language for documents designed to be displayed in a web browser.
- <a href="https://en.wikipedia.org/wiki/CSS" rel="noopener" target="_blank">CSS</a> - Describes how HTML elements are to be displayed on screen, paper, or in other media.
- <a href="https://en.wikipedia.org/wiki/JavaScript" rel="noopener" target="_blank">JavaScript</a> - Programming language that conforms to the ECMAScript specification.
- <a href="https://en.wikipedia.org/wiki/Python_(programming_language)" rel="noopener" target="_blank">Python</a> - Interpreted, high-level and general-purpose programming language

<p id="flp"></p>

### Frameworks, Libraries & Programs Used:

- <a href="hhttps://www.heroku.com/ttps://materializecss.com/" rel="noopener" target="_blank">Materialize</a> - A modern responsive front-end framework based on Material Design
- <a href="https://jquery.com/" rel="noopener" target="_blank">jQuery</a> - Fast, small, and feature-rich JavaScript library.
- <a href="https://git-scm.com/" rel="noopener" target="_blank">Git</a> - Free and open source distributed version control system.
- <a href="https://github.com/" rel="noopener" target="_blank">GitHub</a> - A Git repository hosting service.
- <a href="https://www.heroku.com/" rel="noopener" target="_blank">Heroku</a> - A cloud platform as a service supporting several programming languages.
- <a href="https://www.mongodb.com/" rel="noopener" target="_blank">mongoDB</a> -general purpose, document-based, distributed database built for modern application developers and for the cloud era.
- <a href="https://fontawesome.com/" rel="noopener" target="_blank">Font Awesome</a> - A web font containing all the icons from the Twitter Bootstrap framework, and now many more.
- <a href="https://fonts.google.com/" rel="noopener" target="_blank">Google Fonts</a> - A library of 999 free licensed font families.
- <a href="balsamiq.com" rel="noopener" target="_blank">Balsamiq</a> - Wireframing tool.

<div align="center"><p style="text-align: center"><a href="#top">Back to top ⬆️</a></p></div>

<p id="features"></p>

## 4️⃣ Features List 😲

<p id="existing"></p>

### Existing features:

?????????????????????????????????????????????????????????

<p id="future"></p>

### Future features:

??????????????????????????????????????????????????????????

<div align="center"><p style="text-align: center"><a href="#top">Back to top ⬆️</a></p></div>

<p id="testing"></p>

## 5️⃣ Testing 🔥

<p id="manualtesting"></p>

### Manual Testing:

??????????????????????????????????????????????????????

<p id="ustesting"></p>

 ### User Stories:

 ???????????????????????????????????????????????????????

 <p id="bugs"></p>

 ### Bugs:

 ??????????????????????????????????????????????????????

 <div align="center"><p style="text-align: center"><a href="#top">Back to top ⬆️</a></p></div>
 
 <p id="deployment"></p>

## 6️⃣ Deployment 🚀

This project was developed in GitPod. All developments were pushed to the corresponding repository in GitHub account. App was deployed in Heroku.

In order to deploy the website to Heroku:

- I ensured that app.py, requirements.txt and Procfile files are created and pushed to GitHub.  

- I Created new account on Heroku and I set up new application.

- In 'Deploy' tab I set 'Deployment method' to 'GitHub' so Heroku is automatically updated with GitHub.

- In 'App connected to Github' I set my Github nick and matching repository and clicked 'Connect' button.

- In 'Settings' tab I set 'Config Vars' to match those in app.py file.

- In 'Deploy' tab I clicked "Enable Automatic Deploys".

- To see my deployed app I clicked 'Open App' on the top of Heroku page.

### Run this project locally:

- Select the Repository from the GitHub Dashboard.

- Click the green button labelled 'Code'.

- Click 'Download ZIP'.

- Extract ZIP file on your computer.

- Open folder and open index.html in web browser.

### Clone this project:

- Select the Repository from the GitHub Dashboard.

- Click the green button labelled 'Code'.

- To clone the repository using:
    - HTTPS: under "Clone with HTTPS", click checklist icon.
    - SSH: click Use SSH, then click checklist icon.

- Open Git Bash.

- Change the current working directory to the location where you want the cloned directory.

- Type 'git clone', and then paste the URL you copied earlier.

- Press Enter to create your local clone.

<div align="center"><p style="text-align: center"><a href="#top">Back to top ⬆️</a></p></div>

<p id="credits"></p>

## 7️⃣ Credits 🙏

<p id="code"></p>

### Code:

????????????????????????????????????????????????????

<p id="media"></p>

### Media:

Ads images:
- Playstation 2 - Photo by <a href="https://unsplash.com/@dmjdenise?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Denise Jans</a> on <a href="/s/photos/playstation-3?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Samsung Galaxy S10 - Photo by <a href="https://unsplash.com/@emilianocicero?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Emiliano Cicero</a> on <a href="/s/photos/samsung-galaxy?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Audi r8 - Photo by <a href="https://unsplash.com/@taiscaptures?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Tai's Captures</a> on <a href="/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Jeep - Photo by <a href="https://unsplash.com/@orca23?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Dan Gomer</a> on <a href="/s/photos/jeep?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Jacket - Photo by <a href="https://unsplash.com/@orca23?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Dan Gomer</a> on <a href="/s/photos/jeep?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Shoes - Photo by <a href="https://unsplash.com/@revolt?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">REVOLT</a> on <a href="/s/photos/shoes?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Brush - Photo by <a href="https://unsplash.com/@switch_dtp_fotografie?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Lucas van Oort</a> on <a href="/s/photos/garden-tool?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Wheelbarrow - Photo by <a href="https://unsplash.com/@philhearing?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Phil Hearing</a> on <a href="/s/photos/wheelbarrow?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Chair - Photo by <a href="https://unsplash.com/@itssammoqadam?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Sam Moqadam</a> on <a href="/s/photos/chair?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Couch - Photo by <a href="https://unsplash.com/@martinpechy?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Martin Péchy</a> on <a href="/s/photos/couch?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Bike - Photo by <a href="https://unsplash.com/@robertbye?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Robert Bye</a> on <a href="/s/photos/bike?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Fitness equipment - Photo by <a href="https://unsplash.com/@kellysikkema?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Kelly Sikkema</a> on <a href="/s/photos/weights?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  

<p id="ack"></p>

### Acknowledgments:

- <a href="https://codeinstitute.net" rel="noopener" target="_blank">Code Institute</a>
- <a href="https://stackoverflow.com/" rel="noopener" target="_blank">Stack Overflow</a>
- Code Institute Slack Community.
- My mentor Guido Cecilio for guidance and support.
- My family and friends for their patience and honest critique throughout.

<div align="center"><p style="text-align: center"><a href="#top">Back to top ⬆️</a></p></div>
