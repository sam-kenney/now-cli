# Now

Small CLI tool to print time, date, and weather details to the terminal.

## Installation
To use this CLI, you must have an installation of [Python 3](https://www.python.org/downloads/).

To install this CLI, execute `pip3 install now-info-cli`

## Setup
When you run the `now` command, you will be prompted to input some information.

This includes the following prompts:
| Prompt | Usage |
|---|---|
| Paste in your API Token: | This is needed to access weather data. You can sign up [here](https://openweathermap.org/price). Select the free plan. Your API Key will be emailed to you.  |
| Enter the city you live in: | The name of the city you live in. This is how the weather API determines which data to collect. |

Example:
```
Paste in your API Token: dGhpcyBpcyBhIHRlc3Qgc3RyaW5n
Enter the city you live in: sydney
```

These prompts will only occur on the first execution. This information is stored in your home directory at `.now-cli/.credentials.json` should you ever need to update it.

<code>
<span>[TIME] </span><span style="color:magenta">21:19:06</span><br>
<span>[DATE] </span><span style="color:cyan">Thu Jan 2022</span><br>
<span>[WTHR] </span><span style="color:gold">20°C Clouds</span>
</code>
