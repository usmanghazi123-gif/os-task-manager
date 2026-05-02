# 🧠 OS Task Manager

A Streamlit-based **Process Monitoring System** that simulates basic operating system task management, including process creation, CPU scheduling, and termination.

## 📋 Features

- **Create Processes**: Generate new processes with random attributes (priority, CPU usage, memory)
- **CPU Simulation**: Simulate CPU scheduling using priority-based process selection
- **Kill Processes**: Terminate processes by their PID
- **Live Dashboard**: View all processes and their current state in real-time
- **Process State Management**: Track processes through Ready, Running, and Terminated states

## 🎯 Simulated Process Attributes

- **PID**: Process ID (auto-incremented)
- **Name**: Process name (e.g., P1, P2, P3)
- **Priority**: Priority level (1-10, higher = more priority)
- **CPU (%)**: CPU usage percentage
- **Memory (MB)**: Memory usage in megabytes
- **State**: Current process state (Ready, Running, Terminated)

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/usmanghazi123-gif/os-task-manager.git
   cd os-task-manager
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📱 Usage

Run the application using Streamlit:

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## 🎮 How It Works

### 1. Create Process
Click the "➕ Create Process" button to generate a new process with:
- Auto-incremented PID
- Random priority (1-10)
- Random CPU usage (1-50%)
- Random memory allocation (100-500 MB)
- Initial state: Ready

### 2. Simulate CPU
Click the "⚙️ Simulate CPU" button to:
- Select the highest priority active process
- Set it to "Running" state
- Increase its CPU usage by 5-20%
- Mark all others as "Ready"

### 3. Kill Process
Enter a PID and click "❌ Kill Process" to:
- Set the process state to "Terminated"
- Keep it in the table for reference

## 📊 Process Table

The dashboard displays a live-updating table showing all processes with their current attributes and states.

## 🔧 Technologies Used

- **Streamlit**: Interactive web framework for building data apps
- **Pandas**: Data manipulation and display
- **Python**: Core language

## 📝 Learning Outcomes

This project demonstrates:
- Operating system process management concepts
- Priority-based CPU scheduling algorithms
- Session state management in web applications
- Real-time data visualization

## 🚀 Future Enhancements

- [ ] Add different scheduling algorithms (FCFS, Round Robin, SJF)
- [ ] Implement process state transitions (Ready → Waiting → Running)
- [ ] Add CPU cores simulation
- [ ] Export process logs to CSV
- [ ] Add process memory and I/O statistics
- [ ] Create process timeline visualization

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**usmanghazi123-gif**

## 📞 Support

If you encounter any issues or have suggestions, please open an issue on GitHub.

---

**Happy Process Managing!** 🚀
