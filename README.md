# Hike Calculator

The Hiking Calculator is a Flask web application that estimates the difficulty of a hike based on its distance and total ascent.

**[Live Demo →](https://hiking-app-764764726091.europe-west2.run.app)**

## Purpose

I built this project as a way to combine my interest in hiking with my software development skills. I wanted to explore how information about a hiking route, such as distance and elevation gain, could be used to estimate its difficulty.

The project also provides an opportunity to develop my skills across the full application lifecycle, from building and testing a Flask application, to containerisation and cloud deployment.

Users enter the distance and ascent of a route, and the application calculates the average gradient and provides an overall difficulty rating.

## Tech Stack

| Tech                     | Purpose                      |
| ------------------------ | ---------------------------- |
| Python                   | Application logic            |
| Node.js                  | Tailwind build               |
| Flask                    | Web framework                |
| WTForms                  | Form handling and validation |
| HTML/CSS                 | Frontend templates           |
| Tailwind CSS             | Frontend Styling             |
| pytest                   | Automated testing            |
| Docker                   | Containerisation             |
| GitHub Actions           | CI/CD                        |
| Google Artifact Registry | Docker image storage         |
| Google Cloud Run         | Application hosting          |

## Features

- Takes input of route distance and total ascent, and calculates average gradient and overall difficulty rating.
- Preserves submitted values when displaying results.

## Application Structure

```
hiking_app/
│
├── app/
│ ├── static/
│ ├── templates/
│ ├── **init**.py
│ ├── config.py
│ ├── forms.py
│ └── routes.py
│
├── calculation/
│ ├── **init**.py
│ └── utils.py
│
├── tests/
│ ├── conftest.py
│ ├── test_calculation.py
│ └── test_routes.py
│
├── .github/
│ └── workflows/
│ └── google-cloudrun-docker.yml
│
├── app.py
├── requirements.txt
├── package.json
├── Dockerfile
├── .gitignore
├── .dockerignore
└── README.md
```

- app/ contains the flask application, including routes, forms, templates and configuration.
- calculation/ contains the hiking calculation logic separately from the Flask application.
- tests/ contains automated tests for the application.
- .github/workflows/ contains the GitHub Actions workflow used to build and deploy the application.

## Testing

Currently the automated testing covers the following:

- Homepage loads successfully
- Expected content is displayed
- Valid form submission redirects
- Valid results are displayed
- Invalid input of distance and ascent does not produce results

To run the tests, run the following command in the root directory:

```
python -m pytest
```

## Deployment Architecture

```
GitHub
│
│ push to main
▼
GitHub Actions
│
│ Workload Identity Federation
▼
Google Cloud
│
├── Build Docker image
│
▼
Artifact Registry
│
│ Docker image
▼
Cloud Run
│
├── Secret Manager
│
▼
Live application
```

GitHub Actions automatically builds the Docker image when changes are pushed to the main branch. The image is pushed to Google Artifact Registry and deployed to Google Cloud Run.

GitHub Actions authenticates with Google Cloud using Workload Identity Federation rather than a long-lived service account key.

The Flask secret key is stored in Google Secret Manager and provided to the Cloud Run service at runtime.

## Future Plan

Planned features:

- GPX file upload
- Extract distance and elevation data from GPX files
- Generate an elevation profile
- Analyse steepness throughout a route
- Improve hiking difficulty estimation using route data
- Add a development environment separate from production
- Add a custom domain to the production application

And potentially later:

- Route visualisation
- Map integration
- User accounts
- Saved routes
