# System Monitoring & Automation Scripts

Simple collection of Bash and Python scripts for basic IT support tasks.

## Features

- Log file analysis (.log / .txt)
- File archiving and compression
- System information capture
- Multi-threaded directory scanning

## Structure

- `Task1/` → Log analysis (Bash)
- `Task2/` → File archiving (Python)
- `Task3/` → System info script (Bash)
- `Task4/` → Directory scanner (Python)

## Usage

Run each script individually.

### Requirements

- Bash for `Task1` and `Task3`
- PyCharm for `Task2` and `Task4`

#### Task1: Log analysis

```bash
cd Task1
chmod u+x FileAnalysis.sh
bash FileAnalysis.sh
```

The script opens a menu, asks for the folder to scan, and asks where to save the generated summary file.

#### Task2: File archiving

Open `Task2/task2.py` in PyCharm and run it. Enter the folder path you want to archive. The script creates a dated backup folder and a `.zip` archive inside that location.

#### Task3: System information

```bash
cd Task3
chmod u+x system_info.sh
bash system_info.sh
```

This generates `system_info.txt` with system details such as hostname, CPU info, memory usage, disk space, IP address, and uptime.

#### Task4: Directory scanner

Open `Task4/directory_scanner.py` in PyCharm and run it. Enter the directory path and file extension to search for. The scan results will be printed to the terminal and saved to `results.txt`.
