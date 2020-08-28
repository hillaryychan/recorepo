# recorepo

A script to **re**direct **co**urse **repo**sitories to your GitHub account.

Is this script robust? Probably not.  
But does it work? "It works on my machine" ¯\\\_(ツ)\_/¯

## Requirements

* GitHub personal access token - [creating a personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)
* Python3 - it's time to say goodbye to Python2
* git repositories you want to redirect

## Usage

Say we have a bunch of git repositories (`ass0`, `ass1`, `ass2`, `ass3`) for course COMP3231 that are hosted on another git repository manager. Running

``` sh
python3 recorepo.py <MY_GITHUB_TOKEN> 3231 ass[0-3]
# or
python3 recorepo.py <MY_GITHUB_TOKEN> 3231 ass0 ass1 ass2 ass3
```

will create remote repositories `3231-ass0`, `3231-ass1`, `3231-ass2`, `3231-ass3` on your account and push the master branch to the respective remote repositories.

## Options/Flags

| Options/Flags    | Description                                                         |
| ---              | ---                                                                 |
| `-p`, `--public` | Make the repository public. Repositories are private by default.    |
| `-i`, `--init`   | Initialise repository upon creation. i.e. Add a `README.md`.        |
| `--https`        | Redirect repository to have HTTPS origin path. Uses SSH by default. |
