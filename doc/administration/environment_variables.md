# Environment Variables

CcMS exposes certain environment variables which can be used to override
their defaults values.

## Supported environment variables

Variable | Type | Description
---------|------|------------
`DATABASE_URL` | string | The database URL; By default it's set to `sqlite:///PROJECT_PATH/app.db` where `PROJECT_PATH` is where project is located on your computer.
`SECRET_KEY` | string | String used to encrypt cookies.
`CSRF_SECRET_KEY` | string | String used to encrypt CSRF token (forms security).