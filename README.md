# Packet Analysis and Anomaly Detection Tool
### Name: Navneeth Rajeev Menon
### Roll.No: AA.SC.U3BCA2307091

## Build:

Getting the repo...
```bash
git clone https://github.com/NavneethRM/Project.git
cd Project
```

Install dependencies...
```python
pip install -r requirements.txt
```

## Usage:

For Live capture:
```python
python main.py -l #(Optional -c <int>)
```

offline capture:
```python
python main.py -p #<Path to file>
```

## Result:
Each run will generate Standard output to the Terminal and generate a JSON file containing the output for future reference. It also generates an HTML file holding the said results for better visualization.
