## Install NPM dependencies

```
cd se-group1-project2/ui
npm install
```
### Connecting Backend to Frontend

In the ui/src/config.js file. Make sure you set the config to have the base_url as
http://localhost:8000 for local debugging

```
const config = {
	// Comment this when debugging locally
	// base_url: 'http://3.110.50.141:8000',
	// Uncomment this when debugging locally
	base_url: 'http://localhost:8000',
};
export default config;
```

### Development Mode

In the ui folder of project directory, you can run:

```
npm start
```

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

### Production Optimised Build

```
yarn build
```

Builds the app for production to the `build` folder.\
It bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

### Running frontend tests
```
npm install jest --global
jest __tests__/App.test.jsx
```

# Directory Structure

<pre>
.
  |-.babelrc
  |-.dockerignore
  |-.prettierignore
  |-.prettierrc
  |-assets
  |  |-Block.jpg
  |  |-Block2.png
  |  |-built.png
  |  |-deploy.png
  |  |-jobTrackrLogo.png
  |  |-legacy
  |  |  |-BeforeAfter.png
  |  |  |-built.png
  |  |-LogoJobTrackr.png
  |  |-LogoWithTagline.png
  |  |-part2.mp4
  |  |-part2.png
  |  |-SE_Architecture.png
  |  |-SE_CICD.png
  |-Dockerfile
  |-package-lock.json
  |-package.json
  |-public
  |  |-favicon.ico
  |  |-index.html
  |-README-frontend.md
  |-resources
  |  |-Design.png
  |  |-Features.png
  |  |-readme.md
  |-src
  |  |-App.jsx
  |  |-App.scss
  |  |-Components
  |  |  |-AddApplication
  |  |  |  |-AddApplication.jsx
  |  |  |  |-ApplicationCard.jsx
  |  |  |  |-ApplicationCard.scss
  |  |  |  |-EditApplication.jsx
  |  |  |-CoverLetter
  |  |  |  |-CoverLetter.jsx
  |  |  |  |-CoverLetter.scss
  |  |  |  |-MakeCoverLetter.jsx
  |  |  |-LandingPage
  |  |  |  |-LandingPage.jsx
  |  |  |  |-LandingPage.scss
  |  |  |-LoginPage
  |  |  |  |-LoginPage.jsx
  |  |  |  |-LoginPage.scss
  |  |  |-ManageFiles
  |  |  |  |-AddFile.jsx
  |  |  |  |-ManageFiles.jsx
  |  |  |  |-ManageFiles.scss
  |  |  |-Profile
  |  |  |  |-Profile.jsx
  |  |  |  |-Profile.scss
  |  |  |-QA
  |  |  |  |-AddQuestion.jsx
  |  |  |  |-EditQuestion.jsx
  |  |  |  |-QA.jsx
  |  |  |  |-QA.scss
  |  |  |-RegisterPage
  |  |  |  |-RegisterPage.jsx
  |  |  |  |-RegisterPage.scss
  |  |  |-ResumeSuggestions
  |  |  |  |-MakeSuggestions.jsx
  |  |  |  |-ResumeSuggestions.jsx
  |  |  |  |-ResumeSuggestions.scss
  |  |  |-SavedJobs
  |  |  |  |-AddSavedJob.jsx
  |  |  |  |-EditSavedJob.jsx
  |  |  |  |-SavedJobs.jsx
  |  |  |  |-SavedJobs.scss
  |  |-config.js
  |  |-index.jsx
  |  |-index.scss
  |-webpack.config.js
  |-yarn.lock
  |-__tests__
  |  |-App.test.jsx
</pre>