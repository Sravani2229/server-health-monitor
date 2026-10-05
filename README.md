# Server Health Monitoring App

A simple Python-based server health monitoring application that checks CPU, memory, and disk usage.

## Technologies Used

- Python
- psutil
- Ansible
- AWS EC2
- Git
- GitHub

## Features

- Displays hostname
- Displays operating system
- Displays Python version
- Monitors CPU usage
- Monitors memory usage
- Monitors disk usage
- Shows CPU health status
- Shows memory health status
- Shows disk health status
- Shows overall server health

## Health Status

| Usage | Status |
|---|---|
| Below 70% | HEALTHY |
| 70% - 89% | WARNING |
| 90% or above | CRITICAL |

## Run the Application

```bash
python3 app.py
