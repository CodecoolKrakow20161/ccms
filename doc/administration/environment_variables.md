# Environment Variables

CcMS exposes certain environment variables which can be used to override
their defaults values.

## Supported environment variables

Variable | Type | Description
---------|------|------------
`SQLALCHEMY_DATABASE_URI` | string | The database URL; By default it's set to `sqlite:///PROJECT_PATH/app.db` where `PROJECT_PATH` is where project is located on your computer