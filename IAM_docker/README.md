# IAM DB connection from within a docker container

The solution builds a sample docker image to access Builty DB with IAM authentication similar to the approach described in [Securely connect to Amazon RDS for PostgreSQL with AWS Session Manager and IAM authentication](https://aws.amazon.com/blogs/database/securely-connect-to-amazon-rds-for-postgresql-with-aws-session-manager-and-iam-authentication/)

The platform for the docker image is intentionally restricted to `linux/amd64`
This is the platform that AWS uses for running ECS tasks.

When running locally, make sure you run it in a Linux environment. 
On Windows please use WSL.
On MacOS the solution has been tested on Macbook-Pro with an M1 processor.

## Prerequisites

- IAM user configured with `aws configure`
- Valid DB user/password
- Docker environment installed on your laptop/PC

## Instructions

- Make a copy of `.env.sample` and rename it to `.env`
- In `.env` specify valid values for `DB_USER` and `DB_PASSWORD` (ideally this sensitive info must be stored in AWS Secret Manager)
- Build the docker image with
```
        docker-compose build
```
- Start the container with 
```
        docker-compose up -d
```
- See the logs in `./logs/db_access.log`. This is supposed to look as follows:
```
2024-04-01 06:57:31 __main__ INFO     Connected to Builty DB
2024-04-01 06:57:31 __main__ INFO     Running
2024-04-01 06:57:36 __main__ INFO     Running
2024-04-01 06:57:41 __main__ INFO     Running
2024-04-01 06:57:46 __main__ INFO     Running
2024-04-01 06:57:51 __main__ INFO     Running
2024-04-01 06:57:56 __main__ INFO     Running
2024-04-01 06:58:01 __main__ INFO     Running
...
```
- If the DB connection fails that will be indicated in the log's first line
- Stop and kill the container with
```
        docker-compose down
```
