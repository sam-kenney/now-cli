# Now

Small CLI tool to print time, date, and weather details to the terminal.

## Installation
To use this CLI, you must have an installation of [Python 3](https://www.python.org/downloads/).

Clone this repository to your device. Then execute `pip3 install --editable {./your/installation/path}`

## Setup
In the directory you have cloned this repository to, create an environment file called `.env`.

In this file, add the following variables:
| Variable Name | Usage |
|---|---|
| WEATHER_API_KEY | This is needed to access weather data. You can sign up [here](https://openweathermap.org/price). Select the free plan. Your API Key will be emailed to you.  |
| CITY | The name of the city you live in. This is how the weather API determines which data to collect. |

Example:
```sh
export WEATHER_API_KEY="dGhpcyBpcyBhIHRlc3Qgc3RyaW5n"
export CITY="sydney"
```
