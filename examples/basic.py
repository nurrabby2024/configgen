"""Minimal example for ConfigGen."""

from configgen import configgen


def main():
 runner = configgen({"name": "ConfigGen", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()