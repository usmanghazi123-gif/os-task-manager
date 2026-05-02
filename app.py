import streamlit as st
import random
import pandas as pd

# -------------------------------
# Initialize Session State
# -------------------------------

if "processes" not in st.session_state:
    st.session_state.processes = []
    st.session_state.pid_counter = 1

# -------------------------------
# Functions
# -------------------------------

def create_process():
    """Create a new process with random attributes"""
    pid = st.session_state.pid_counter
    name = f"P{pid}"
    priority = random.randint(1, 10)
    memory = random.randint(100, 500)
    cpu = random.randint(1, 50)
    state = "Ready"

    st.session_state.processes.append({
        "PID": pid,
        "Name": name,
        "Priority": priority,
        "CPU (%)": cpu,
        "Memory (MB)": memory,
        "State": state
    })

    st.session_state.pid_counter += 1


def kill_process(pid):
    """Terminate a process by PID"""
    for p in st.session_state.processes:
        if p["PID"] == pid:
            p["State"] = "Terminated"
            break


def simulate_cpu():
    """Simulate CPU scheduling using priority-based selection"""
    active = [p for p in st.session_state.processes if p["State"] != "Terminated"]

    if not active:
        st.warning("No active processes available!")
        return

    # Select highest priority process
    running = max(active, key=lambda x: x["Priority"])

    # Reset states
    for p in active:
        p["State"] = "Ready"

    # Set one process to running
    running["State"] = "Running"
    running["CPU (%)"] += random.randint(5, 20)


# -------------------------------
# UI Layout
# -------------------------------

st.set_page_config(page_title="Process Monitoring System", layout="wide")

st.title("🧠 Process Monitoring System (Task Manager Simulation)")

st.markdown("Simulates basic OS process management including scheduling, execution, and termination.")

# Buttons Row
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➕ Create Process"):
        create_process()
        st.rerun()

with col2:
    if st.button("⚙️ Simulate CPU"):
        simulate_cpu()
        st.rerun()

with col3:
    pid_to_kill = st.number_input("Enter PID to Kill", min_value=1, step=1)
    if st.button("❌ Kill Process"):
        kill_process(int(pid_to_kill))
        st.rerun()

st.divider()

# -------------------------------
# Display Process Table
# -------------------------------

if st.session_state.processes:
    df = pd.DataFrame(st.session_state.processes)
    st.subheader("📊 Process Table")
    st.dataframe(df, use_container_width=True)
else:
    st.info("No processes created yet. Click 'Create Process' to begin.")
