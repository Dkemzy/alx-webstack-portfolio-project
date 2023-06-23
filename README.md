[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />
<div align="center">
  <a href="https://github.com/Dkemzy/alx-webstack-portfolio-project/">
    <img src="/static/images/logo.png" alt="Logo" width="600" height="250">
  </a>

  <h3 align="center">Expense Tracking</h3></h3>

  <p align="center">
    An App To Track Expenses
    <br />
    <br />
    <br />
    <a href="http://thehacker1.pythonanywhere.com/">Landing Page</a>
    ·
    <a href="">Blog Article</a>
    .
    <a href="https://github.com/Dkemzy/alx-webstack-portfolio-project/issues">Report Issues</a>
    ·
    <a href="https://github.com/Dkemzy/alx-webstack-portfolio-project/issues">Request Feature</a>
  </p>
</div>

## Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Related projects](#related-projects)
- [Licensing](#licensing)

## Introduction

This project consist of developing an expense tracker app for managing personal finances that allows users to track their expenses, categorize them, and generate reports.

Deployed Project link: [Deployed Project](https://watch.screencastify.com/v/ZX2Sxa7mAuOpo4VnWKyU)

Final Project Blog Article: [Blog Article]()

### Authors

Robert Njonjo - [Github](https://github.com/M1urray) / [Linkedin](https://www.linkedin.com/in/robert-njonjo)

Dennis Kamau - [Github](https://github.com/Dkemzy) / [Linkedin](https://www.linkedin.com/in/kamau-dennis-b3155b153)

Rim EL FILALI - [Github](https://github.com/Rima119) / [Linkedin](https://www.linkedin.com/in/rim-el-filali-0710a6269/)

### Built With

<p align="left"> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a> </p>

### Features

- User authentication
- Track expenses and categorize them for easy analysis.
- Add/Edit/Delete Expenses.
- View already existing expenses
- A 50/30/20 model of money management Calculator

## Installation

To use the Expense Tracker, follow these steps:

1. Clone the repository:

```shell
git clone https://github.com/Dkemzy/alx-webstack-portfolio-project.git
```

2. Navigate to the project directory:

```shell
cd alx-webstack-portfolio-project
```
3. Install the dependencies:
``` bash
npm install
```
4. Set up the database:

- Create a new PostgreSQL database.
- Rename the .env.example file to .env and update the DB_CONNECTION configuration with your database credentials.

5. Run the database migrations:

``` shell
npm run migrate
```

6. Access the Expense Tracker in your web browser:

``` arduino
http://localhost:5000
```
or *RUN The Program Directly*

1. Clone the repository:

```shell
git clone https://github.com/Dkemzy/alx-webstack-portfolio-project.git
```

2. Navigate to the project directory:

```shell
cd alx-webstack-portfolio-project
```
3. Run the application:

``` python
python main.py
```

## Usage

1. Register for a new account by providing your details and creating a username and password.

2. Log in to your account using your credentials.

3. Once logged in, you will be able to:

- Add new expenses by providing the necessary details such as date, category, amount, and description.
- View your expense list, categorized by date and category.
- Edit or delete existing expenses.
- Generate reports to analyze your spending patterns and track your financial goals.
- Manage your user profile and update your account settings.

4. Use the Expense Tracker regularly to record your expenses and gain better control over your finances.

## Contributing

If you have issues, questions or create a pull request.

For suggestions follow these steps:

1. Fork this repository
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request

Please ensure your pull request adheres to the following guidelines:

- Alphabetize your entry.
- Search previous suggestions before making a new one, as yours may be a duplicate.
- Suggested READMEs should be beautiful or stand out in some way.
- Make an individual pull request for each suggestion.
- New categories, or improvements to the existing categorization are welcome.
- Keep descriptions short and simple, but descriptive.
- Start the description with a capital and end with a full stop/period.
- Check your spelling and grammar.
- Make sure your text editor is set to remove trailing whitespace.
- Use the `#readme` anchor for GitHub READMEs to link them directly

Thank you for your suggestions!

## Related projects

- [Expenses](https://github.com/jakubgarfield/expenses)

- [Expenso](https://github.com/Spikeysanju/Expenso)

- [MyExpenses](https://github.com/mtotschnig/MyExpenses)

## Licensing

This project is licensed under the [MIT License](https://github.com/Dkemzy/alx-webstack-portfolio-project/blob/main/LICENSE) - see the LICENSE file for details.

[contributors-shield]: https://img.shields.io/github/contributors/Dkemzy/alx-webstack-portfolio-project.svg?style=for-the-badge
[contributors-url]: https://github.com/Dkemzy/alx-webstack-portfolio-project/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Dkemzy/alx-webstack-portfolio-project.svg?style=for-the-badge
[forks-url]: https://github.com/Dkemzy/alx-webstack-portfolio-project/forks
[stars-shield]: https://img.shields.io/github/stars/Dkemzy/alx-webstack-portfolio-project.svg?style=for-the-badge
[stars-url]: https://github.com/Dkemzy/alx-webstack-portfolio-project/stargazers
[issues-shield]: https://img.shields.io/github/issues/Dkemzy/alx-webstack-portfolio-project.svg?style=for-the-badge
[issues-url]: https://github.com/Dkemzy/alx-webstack-portfolio-project/issues
[license-shield]: https://img.shields.io/github/license/Dkemzy/alx-webstack-portfolio-project.svg?style=for-the-badge
[license-url]: https://github.com/Dkemzy/alx-webstack-portfolio-project/blob/main/LICENSE
