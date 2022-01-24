"""Module containing Now CLI."""
import json
import os
from datetime import datetime
from typing import Dict

import click

from colorama import Fore, init

from enforce_typing import enforce_typing

import requests


@click.group(invoke_without_command=True)
def cli():
    """Command Line Interface for time, date, and weather information."""
    init(autoreset=True)
    now: datetime = datetime.now()
    print(
        f"{_time(now)}{Fore.RESET}\n{_date(now)}{Fore.RESET}\n{_weather()}{Fore.RESET}"
    )


@enforce_typing
def _time(now: datetime) -> str:
    """
    Return the current time.

    now: datetime
        A datetime.now() object.
    """
    if not isinstance(now, datetime):
        raise ValueError(
            f"Passed in argument is of type {now.__qualname__}, must be datetime."
        )
    return f"[TIME] {Fore.MAGENTA}{now.strftime('%H:%M:%S')}"


@enforce_typing
def _date(now: datetime) -> str:
    """
    Return the current date.

    now: datetime
        A datetime.now() object.
    """
    if not isinstance(now, datetime):
        raise ValueError(
            f"Passed in argument is of type {now.__qualname__}, must be datetime."
        )
    return f"[DATE] {Fore.CYAN}{now.strftime('%a %b %d %Y')}"


@enforce_typing
def _weather() -> str:
    """Return the current weather at a specified city."""
    config: Dict[str, str] = _get_config()
    api_key: str = config["WEATHER_API_KEY"]
    city: str = config["CITY"]

    resp = requests.get(
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    ).json()
    try:
        temp: str = str(int(resp["main"]["feels_like"] - 273.15)) + "°C"
        weather: str = resp["weather"][0]["main"]

        return f"[WTHR] {Fore.YELLOW}{temp} {weather}"
    except KeyError:
        return (
            f"[WTHR] {Fore.YELLOW}Unavailable: API Key is incorrect or service is down."
        )


@enforce_typing
def _get_config() -> Dict[str, str]:
    """Load user config file for now CLI."""
    dir_path: str = os.path.join(".now-cli")
    config_path: str = os.path.join(".now-cli", ".credentials.json")

    if os.path.exists(dir_path):
        if os.path.isfile(config_path):
            with open(config_path) as file:
                return json.load(file)
        else:
            _create_config_file(config_path)
            with open(config_path) as file:
                return json.load(file)

    else:
        _create_config_dir(dir_path, config_path)
        with open(config_path) as file:
            return json.load(file)


@enforce_typing
def _create_config_dir(dir_path: str, config_path: str) -> str:
    """Create configuration directory."""
    if os.path.exists(dir_path):
        _create_config_file(config_path=config_path)
        return config_path
    else:
        os.makedirs(dir_path)
        _create_config_file(config_path=config_path)
        return config_path


@enforce_typing
def _create_config_file(config_path: str) -> str:
    """Create configuration file."""
    if os.path.isfile(config_path):
        return config_path
    else:
        with open(config_path, "w") as file:
            api_token: str = input("Paste in your API Token: ")
            city: str = input("Enter the city you live in: ")
            data = {
                "WEATHER_API_KEY": api_token,
                "CITY": city.lower(),
            }
            json.dump(data, file)
        return config_path


if __name__ == "__main__":
    cli()
