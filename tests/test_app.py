def hello_world():
    print("Hello DevOps from Ubuntu!")

if __name__ == "__main__":
    hello_world()

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.9"
      - name: Install dependencies
        run: pip install pytest
      - name: Run tests
        run: python -m pytest\
