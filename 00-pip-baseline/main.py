import click
import httpx
import flask
from importlib.metadata import version

def main():
    print(f"flask=={version('flask')} (HTTPS archive of git commit)")
    print(f"httpx=={version('httpx')} (HTTPS URL)")
    print(f"click=={version('click')} (PyPI registry)")
    print("SUCCESS - pip baseline: all packages imported!")

if __name__ == "__main__":
    main()
