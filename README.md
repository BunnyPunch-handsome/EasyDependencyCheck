
[English](README.md) | [中文](README.zh.md)

# EasyDependencyCheck

## Overview

EasyDependencyCheck is a script based on the open-source project [Dependency Check](https://github.com/jeremylong/DependencyCheck). This script aims to simplify the usage of Dependency Check for vulnerability scanning, especially for those who have limited internet access for pulling the NVD database or find Dependency Check challenging to use.

**WARNING:** This project is intended solely to improve cybersecurity and reduce vulnerabilities. It is strictly prohibited to use this project for illegal purposes. It is intended for learning and communication only. Any misuse of this project is not the responsibility of the author.

This is a test version and may have some imperfections. The NVD database will be maintained regularly to ensure up-to-date vulnerability data.

## Requirements

- Python 3  (If you use an exe to run the program, then the Python environment is not necessary)
- Docker

## Installation and Usage

### Load Dependency Check Docker Image

You can pull the latest image from Docker Hub: docker pull obsidian6362/easy-dependency-check:latest.

### Cloning the Repository

1. Clone the repository: git clone https://github.com/BunnyPunch-handsome/EasyDependencyCheck.git.
2. Navigate to the cloned repository directory: cd EasyDependencyCheck.

### Running the Script or Executable File

You can either run the script using Python or use the pre-built executable file (for Windows).

#### Using Python Script

To run the script, execute the following command: python EasyDependencyCheck.py.

#### Using Executable File (Windows)

1. Download the pre-built executable file from the releases page.
2. Run the executable file by double-clicking it.

### Script Interface Usage

1. Jar File: Click "Browse" to select the jar file you want to scan.
2. Report Path: Click "Browse" to select the path where you want to save the report.
3. Vulnerability DB Update: Select "Yes" if you want to update the vulnerability database, and enter the NVD API Key if prompted.
4. Logs: View the log output of the scan process.
5. Scan Button: Click "Scan" to start the vulnerability scan.

### Folder Structure

- EasyDependencyCheck.py: The main script file for running the vulnerability scans.
- README.md: This documentation file.

## Notes

- Ensure you have Docker installed and running on your system.
- This script requires an internet connection to pull the latest vulnerability data if updating the database.

## Disclaimer

This project is provided "as is" without any warranties of any kind. The author takes no responsibility for any misuse of the project. Use at your own risk. The author will not be held liable for any damages or losses arising from the use of this project. Users are responsible for ensuring their own compliance with local laws and regulations. This project is intended for educational and research purposes only. Use of this project for any unauthorized purposes is strictly prohibited.
