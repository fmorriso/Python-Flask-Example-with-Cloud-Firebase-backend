from flask import Flask
from pathlib import Path


def find_file(filename: str, search_path: str = '.'):
    print(f'Searching for file {filename} starts at directory: {search_path}')
    return next(Path(search_path).rglob(filename), None)

script_path = Path(__file__).resolve()
script_dir = script_path.parent  # Directory of the script

print("Full script path:", script_path)
print("Script directory:", script_dir)

full_path = find_file('fpm-flask-example-firebase-key.json', str(script_dir) )
print(f'{full_path=}')
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
