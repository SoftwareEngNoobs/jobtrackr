# JobTrackr Application

<p align="center">
  <img src="./ui/assets/LogoWithTagline.png" alt="Logo"/>
</p>

[![DOI](https://zenodo.org/badge/870736387.svg)](https://doi.org/10.5281/zenodo.14020850)
![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub](https://img.shields.io/badge/Language-JavaScript-blue.svg)
![Yarn](https://img.shields.io/badge/Yarn-v1.22.19-green.svg)
![npm](https://img.shields.io/badge/npm-v8.9.0-green.svg)
![Node](https://img.shields.io/badge/node-v16.15.1-green.svg)
![Python](https://img.shields.io/badge/python-v3.10-green.svg)

![Open issues](https://img.shields.io/github/issues-raw/SoftwareEngNoobs/jobtrackr)
![Closed issues](https://img.shields.io/github/issues-closed-raw/SoftwareEngNoobs/jobtrackr?color=bright-green)
[![Frontend-build](https://github.com/SoftwareEngNoobs/jobtrackr/actions/workflows/frontend_build_test.yml/badge.svg)](https://github.com/SoftwareEngNoobs/jobtrackr/actions/workflows/frontend_build_test.yml)
[![Backend-build](https://github.com/SoftwareEngNoobs/jobtrackr/actions/workflows/backend_build.yml/badge.svg)](https://github.com/SoftwareEngNoobs/jobtrackr/actions/workflows/backend_build.yml)
[![Backend-Test](https://github.com/SoftwareEngNoobs/jobtrackr/actions/workflows/code_coverage.yml/badge.svg)](https://github.com/SoftwareEngNoobs/jobtrackr/actions/workflows/code_coverage.yml)
[![Style-Checker](https://github.com/SoftwareEngNoobs/jobtrackr/actions/workflows/style_checker.yml/badge.svg)](https://github.com/SoftwareEngNoobs/jobtrackr/actions/workflows/style_checker.yml)
[![Autopep8](https://github.com/SoftwareEngNoobs/jobtrackr/actions/workflows/autopep8.yml/badge.svg)](https://github.com/SoftwareEngNoobs/jobtrackr/actions/workflows/autopep8.yml)

![Repo Size](https://img.shields.io/github/repo-size/SoftwareEngNoobs/jobtrackr?color=brightgreen)
[![GitHub Release](https://img.shields.io/github/release/SoftwareEngNoobs/jobtrackr)](https://github.com/SoftwareEngNoobs/jobtrackr/releases/)
[![codecov](https://codecov.io/github/SoftwareEngNoobs/jobtrackr/branch/release-1.1/graph/badge.svg?token=NH4U7HKW8N)](https://codecov.io/github/SoftwareEngNoobs/jobtrackr)


---

### Documentation for the project is available [here](https://SoftwareEngNoobs/jobtrackr/docs/backend/index.html).

---

## Table of Contents

- [Description](#description)
- [What's New?](#whats-new)
- [Development Tech Stack](#development-tech-stack)
- [Deployment Tech Stack](#deployment-tech-stack)
- [Architecture](#architecture)
- [CI/CD Pipeline](#cicd-pipeline)
- [Application Demo](#application-demo)
- [Getting Started](#getting-started---developer)
- [Development Specifications](#development-tech-stack)
  - [Backend](./backend/README-backend.md)
  - [Frontend](./ui/README-frontend.md)
- [License](./LICENSE)
- [Tools](#tools)
- [Contributors](#contributors)
- [Help](#help)

## Description

Are you someone in the process of looking for a job? Then you can relate to the tiresome and inefficient process. Therefore, excel sheets that are complex and disorganized must go! Every job-related data can be managed by our JobTrackr Application, including your job profile, applications, status, important dates, notes, saved applications, job descriptions, recruiter details, compensation and offer package, and more. It even supports even managing your files and offers a Question Answer Scratchpad for you to save answers to commonly asked questions during job applications. Now, we've pushed the limits to make your process even more convenient. Need to improve your resume? Do you need to create cover letters? Don't worry, we now support resume suggestions and cover letter creation with AI!

## What's New?
### Before
Save Applications
* Applications could be created and saved. These applications persist.

Track Applications
* Applications can be tracked by their status.

Manage Files
* Important files such as resumes or CVs could be uplodaed to AWS S3.

Question/Answer Scratchpad
* Common questions and answers can be stored for convenience.

Continuous Integration
* Deployment was done through GitHub Actions. With Jenkins, Ansible, and GitHub webhooks.

### After
Extra files not stored in backend
* Previously, when files from AWS S3 were sent to the user, they would be downloaded and kept in the backend directory as a side consequence. We have updated it so that the these files will not clog up our repository

Resume suggestions
* Users can now get resume suggestions! Have you ever wanted to get advice about your resume according to a job description but not know who to ask? Well, now you can ask AI to do it for you.

Cover letter generation
* Users can now generate cover letters for a specific job application with their resume! It makes it super convenient for jobs that keep asking for you to write 300+ words!

Cover Letters and Resume Suggestions can be downloaded
* Users can download the AI generated content as a .txt file to save!

Ollama integration
* We've integrated Llama3.2, a powerful AI system that gives seamless responses. Even better is that it is open source! You won't have to worry about cost!

UI update! Dropdown and company logos can now be added! 
> Are aesthetics important to you? Well do not fear, some new components are here!
* Dropdown
  * You can now move applications around with a dropdown instead of having to modify the application each time! Makes it way more convenient.
* Logos
  * You can now insert image links to display company logos on applications! This is for aesthetics! Now you can look at pictures instead of just looking only at text.

[![JobTrackr Animated Video](https://img.youtube.com/vi/z4bh9J7PbMI/maxresdefault.jpg)](https://youtu.be/z4bh9J7PbMI)

## Development Tech Stack

<p align="center">
<img src="./ui/assets/built.png" width="65%" style="margin-left:50px">
</p>

- `react 18.2.x`
- `babel 7.19.x`
- `webpack cli 4.x`
- `sass` (Dart Sass)
- `Python 3.8+`
- `Flask`
- `MongoDB`
- `Ollama`
- `LangChain`

Note: This repository is configured with [Dart-sass](https://github.com/sass/dart-sass) and not [Node Sass].

## Deployment Tech Stack

<p align="center">
<img src="./ui/assets/deploy.png" width="65%" style="margin-left:50px">
</p>

- `AWS`
- `Docker`
- `Jenkins`
- `Ansible`

## Architecture

<p align="center">
  <img src="./ui/assets/SE_Architecture.png" width="50%" height="50%"/></a>
</p>

## CI/CD Pipeline

<p align="center">
  <img src="./ui/assets/SE_CICD.png" width="50%" height="50%"/></a>
</p>

## Application Demo

[![JobTrackr App Demo](https://img.youtube.com/vi/pfs38jh5hPs/maxresdefault.jpg)](https://youtu.be/9xIDV6a-Prs)


## Getting Started - Developer

### Prerequisites

- npm 8.x (8.9 recommended)
- yarn 1.22.x
- Python 3.8+

### Installation

1. Clone the repository

```
git clone https://github.com/SoftwareEngNoobs/jobtrackr.git
```

2. [Backend Setup](./backend/README-backend.md)
3. [UI Setup](./ui/README-frontend.md)
4. [Workflow Setup](./.github/workflows)

## Tools

- Preetier Code Formatter
- PyLint with Flake8

## Third-Party Tools

- [MongoDB](https://www.mongodb.com/)
- [AWS](https://aws.amazon.com/)
- [Jenkins](https://www.jenkins.io/)
- [Ansible](https://www.ansible.com/)
- [ngrok](https://ngrok.com/)
- [Ollama](https://ollama.com/)
- [Llama3.2](https://ollama.com/library/llama3.2)

## Future Milestones
- Drag and Drop Kanban Board
- Upload Generated Cover Letters
- Host the application on AWS EC2
- Web Scraper for Job Descriptions from Indeed
- Markdown formatting for notes
- Migrate from jest testing framework to vitest

## Contributors

<table>
  <tr>
 <td align="center"><a href="https://github.com/mahimdashora"><img src="https://avatars.githubusercontent.com/u/60029463?v=4" width="100px;" alt=""/><br /><sub><b>Mahim Dashora</b></sub></a></td>
<td align="center"><a href="https://github.com/VarunMK"><img src="https://avatars.githubusercontent.com/u/52526572?v=4" width="100px;" alt=""/><br /><sub><b>Varun MK</b></sub></a></td>
<td align="center"><a href="https://github.com/kr1k-boop"><img src="https://avatars.githubusercontent.com/u/71825347?v=4" width="100px;" alt=""/><br /><sub><b>Krithika Ragothaman</b></sub></a></td>
  </tr>
<tr>
    <td align="center"><a href="https://github.com/Kethly"><img src="https://avatars.githubusercontent.com/u/57457270?v=4" width="100px;" alt=""/><br /><sub><b>Thien Do</b></sub></a></td>
    <td align="center"><a href="https://github.com/Nlorenc2760"><img src="https://avatars.githubusercontent.com/u/99928198?s=400&u=cc7ab1019415d06c72c81840ed406675c4b0af2a&v=4" width="100px;" alt=""/><br /><sub><b>Nathan Lorenc</b></sub></a></td>
    <td align="center"><a href="https://github.com/jfmcdavitt"><img src="https://avatars.githubusercontent.com/u/57042681?v=4" width="100px;" alt=""/><br /><sub><b>Jake McDavitt</b></sub></a></td>
</tr>
<tr>
    <td align="center"><a href="https://github.com/jayrajmulani"><img src="https://avatars.githubusercontent.com/u/39649967?v=4" width="100px;" alt=""/><br /><sub><b>Jayraj Mulani</b></sub></a></td>
    <td align="center"><a href="https://github.com/Yashasya"><img src="https://avatars.githubusercontent.com/u/40204748?s=400&u=7a61d3a684ea684e3a2b3f2c3e83d90fd3e8ac0a&v=4" width="100px;" alt=""/><br /><sub><b>Yashasya Shah</b></sub></a></td>
    <td align="center"><a href="https://github.com/Dhrumil0310"><img src="https://avatars.githubusercontent.com/u/50771715?v=4" width="100px;" alt=""/><br /><sub><b>Dhrumil Shah</b></sub></a></td>
    <td align="center"><a href="https://github.com/Harshil47"><img src="https://avatars.githubusercontent.com/u/66715871?v=4" width="100px;" alt=""/><br /><sub><b>Harshil Sanghavi</b></sub></a></td>
    <td align="center"><a href="https://github.com/anishasc99"><img src="https://avatars.githubusercontent.com/u/67101520?v=4" width="100px;" alt=""/><br /><sub><b>Anisha Chazhoor</b></sub></a></td>
</tr>
  <tr>
    <td align="center"><a href="https://github.com/rahulrk2303"><img src="https://avatars.githubusercontent.com/u/30636208?v=4" width="100px;" alt=""/><br /><sub><b>Rahul Rangarajan Kannan</b></sub></a></td>
    <td align="center"><a href="https://github.com/ekanshsinghal"><img src="https://avatars.githubusercontent.com/u/15945880?v=4" width="100px;" alt=""/><br /><sub><b>Ekansh Singhal</b></sub></a></td>
    <td align="center"><a href="https://github.com/gowtham-sathyan"><img src="https://avatars.githubusercontent.com/u/37440294?v=4" width="100px;" alt=""/><br /><sub><b>Gowtham Sathyan</b></sub></a></td>
    <td align="center"><a href="https://github.com/sbkrishna123"><img src="https://avatars.githubusercontent.com/u/89660642?v=4" width="100px;" alt=""/><br /><sub><b>Supriya Krishna</b></sub></a></td>
  </tr>
</table>

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Help
Need help?

If you need any help with our software, please contact jobtrackr.github@gmail.com.
