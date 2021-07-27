#!/usr/bin/env python
from brain_games.welcome_cli import name
from brain_games.games.cli_calc import play_calc


def main():
    print(play_calc())


if __name__ == '__main__':
    main()
