"""Module containing Now CLI."""
from errno import EMFILE
import os
from datetime import datetime

import click

from colorama import Fore, init

from dotenv import load_dotenv

from enforce_typing import enforce_typing

import requests


@click.group(invoke_without_command=True)
def cli():
    """Command Line Interface for time, date, and weather information."""
    init(autoreset=True)
    load_dotenv()
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
    api_key: str = os.environ["WEATHER_API_KEY"]
    city: str = os.environ["CITY"]

    resp = requests.get(
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    ).json()

    temp: str = str(int(resp["main"]["feels_like"] - 273.15)) + "°C"
    weather: str = resp["weather"][0]["main"]

    return f"[WTHR] {Fore.YELLOW}{temp} {weather}"


if __name__ == "__main__":
    cli()
