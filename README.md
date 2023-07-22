# Project Title

A brief description of what this project does.

## Installation

1. Clone the repository: `git clone https://github.com/sreeramsutraye/paste_lockly.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Start the server:
   `python3 manage.py makemigrations`
   `python3 manage.py migrate`
   `python3 manage.py runserver`

## Usage

Developing a web app where people can anonymously share text snippets.
What does it contain:

1. A form where we can enter text and create a shareable URL.
2. Shareable URL should lead to the view-only snippet.
3. Optionally, the creator of the snippet URL can add a secret key which will be used to encrypt the content in the database.
4. The viewer must supply the key to decrypt the content.
