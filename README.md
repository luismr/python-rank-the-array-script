# Python Rank Array Script

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

A Python script that ranks an array of scores according to specific rules:
- Highest score gets rank 1
- Second highest score gets rank 2
- Tied scores receive the same rank
- Ranks are returned in the same order as the input scores

## Project Structure

```
.
├── LICENSE.md
├── README.md
├── requirements.txt
├── .gitignore
└── src/
    ├── rank_array.py
    └── test_rank_array.py
```

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone git@github.com:luismr/python-rank-the-array-script.git
cd python-rank-the-array-script
```

2. Create and activate a virtual environment:

### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The script provides a function `rank_array(scores)` that takes a list of scores as input and returns a list of ranks.

Example:
```python
from src.rank_array import rank_array

scores = [9, 3, 6, 10]
ranks = rank_array(scores)
print(ranks)  # Output: [2, 4, 3, 1]
```

## Running Tests

To run the test suite:
```bash
pytest src/test_rank_array.py -v
```

For coverage report:
```bash
pytest src/test_rank_array.py --cov=src --cov-report=term-missing
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. 