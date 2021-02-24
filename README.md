# Milestone Project 2

---

<p id="top"></p>

## Buy & Sell Marketplace

This project is a summary of study from the eight, ninth and tenth modules of the Full Stack Developer Course - Python Fundamentals, Practical Python and Data Centric Development, to create a fully Mobile Responsive CRUD Web Application.

Buy & Sell app is an online marketplace where users can buy and sell items. Purpose of this project is to create simple app where users can add new ads, browse and search for items and update or delete ads they added.

## Table of contents

- <a href="#project">Project Construction 👷</a>
- <a href="#ux">User Experience Design 🧠</a>
    - <a href="#us">User Stories</a>

<p id="project"></p>

## 1️⃣ Project Construction 👷

This application contains the key CRUD requirement functionality and utilises a data handling document based database, MongoDB. Functionality is created using Flask, HTML5, CSS and JavaScript. Bootstrap framework was used in building fronted structure to make sure app is responsive as possible and can be used on multiple screen sizes.

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
- For more permissions Guest can register and login using quick registration form.
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
- Edit and Delete buttons are visible for ads created by user only.
4. As a Registered user, I want 'Profile' page where I can see my ads and statistics.
-  Registered user will see 'Profile' tab in navigation after Log In.
5. As a Registered user, I want to 'Log Out'.

### Admin:

1. As Admin, I want to ad new 'Categories'
- Admin can ad new 'Categories' by clicking 'Ad Category' in 'Profile' page.
2. As Admin, I want delete or update any ad.
Edit and Delete buttons are visible for all ads.
3. As, Admin I want to remove 'Registered User'.
Admin can remove users by clicking 'Remove User' button in 'Profile' page.
4. As, Admin I want to see app statistics.
Admin can see various statistics in 'Profile' page.

### Developer:

1. As a Developer, I want to create database application app using Python and Flask.
2. As a developer, I want to create fully responsive app.
- Application is fully responsive thanks to Materialize framework.
