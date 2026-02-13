# {{ cookiecutter.app_name }}

{{ cookiecutter.description }}

## Development

This project uses uv to manage dependencies and run the application. 
Pre-commit hookes are managed using prek.
Versioning is based on git tags.
The build backend includes a mechanism to automatically compile locales when building the package.

Make messages using ``ENV_PATH="../ephios/.env" django-admin makemessages -a``
