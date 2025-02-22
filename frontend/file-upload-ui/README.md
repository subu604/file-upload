# angular-file-upload #


<h4 align="center">an angular application template for user registration and file upload</h4>


<p align="center">
    <a alt="Angular">
        <img src="https://img.shields.io/static/v1?label=Angular&message=9.0.7&color=blue" />
    </a>
    <a alt="Typescript">
        <img src="https://img.shields.io/static/v1?label=Typescript&message=3.7.5&color=brightgreen" />
    </a>
    <a alt="JWT">
        <img src="https://img.shields.io/static/v1?label=JWT&message=0.9.1&color=green" />
    </a>
</p>


## Overview ##
This is an angular application to demonstrate user registration and authentication functionality using backend django JWT (JSON Web Tokens).

This application can be used as a template to create a standalone client side registration UI and based on the user credentials uploads a file and fetches the uploaded files.

This application uses a backened server built in my another project, which authenticates a user and generates JSON Web Token for valid request. This project can be accessed from the following backend zip folder attached on the very same email.

Any other authentication server can also be used with this client side angular application as long as it is able to authenticate a user and send back a valid token.

## features ##
  - Registration and login UI using angular.
  - Utilizes angular modules.
  - Utilizes angular routing.
  - Utilizes angular Components.
  - Utilizes angular Services.
  - Utilizes angualar forms modules to provide most checks on registrations and login forms.
  - Stores token in **localstorage** for client side session check.
  - Utilizes **HTTPInterceptor** to attach token in 'Authorization' header once user is logged in.
  - Can be plugged with any authentication srever which is capable of sending valid tokens after autheticating a user.
  - Uses Authentication guard (implementing **canActivate**) to check and redirect to login if user session is not valid.


## Setting up Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).