#!/usr/bin/env python
from brain_games.welcome_cli import name
from brain_games.games.cli_gcd import play_gcd


def main():
    print(play_gcd())


if __name__ == '__main__':
    main()
