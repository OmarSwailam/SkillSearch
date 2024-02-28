# SkillSearch
Skill Search is a website that allows users to create a professional portfolio to showcase their skills and projects. Additionally, visitors can search for individuals based on certain skills or job titles.

Used in this project:
CustomUser - CustomManager - ModelForms - Signals - CustomTemplateTags - Search - Pagination

[Demonstration video](https://youtu.be/22Q2D44pILE?si=bID70H7IY2edmmvL)


Features:
  -	Implemented a CustomUser Model so users can create their account using Email.
  -	Used Signals for profile creating after registration.
  -	Integrated Search functionality that enables employers or clients to find potential candidates.
  -	Designed pagination for more efficient navigation through the set of search results.
  -	Designed the ability to upload multiple images when creating a portfolio project.


## Installation

#### Clone repository
```
  git clone https://github.com/OmarSwailam/skillsearch.git
```

#### Create a virtualenv(optional)
```
  python3 -m venv venv
```

#### Activate the virtualenv
```
  .venv/scripts/activate
```
#### Install all dependencies
```
   pip install -r requirements.txt
```
#### Migrate DB changes
```
  python manage.py migrate
```
#### Run application
```
  python manage.py runserver
```

Author:
  Omar Swailam
