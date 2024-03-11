# https://docs.docker.com/engine/

# Terminal commands: 
# docker pull mysql # downloads the MySQL image from Docker Hub, which is a public repository for Docker images

import streamlit as st
from SQLConnect import SQLConnectDocker as SQLConnect
import customize_gui as gui
gui = gui.gui()

gui.setup(wide=True,text="This code acts as the client to a MySQL server running in a Docker container.")

st.markdown("# MySQL Web Client")

if "sql" not in st.session_state:
    st.session_state.sql = SQLConnect()
    st.session_state.sql.connect()
if "sql" in st.session_state:
    sql = st.session_state.sql

with st.sidebar:
    result = sql.get_summary()
    Databases = st.empty()
    with Databases: st.table(result)
    "---"

    st.write('Docker installed:', sql.docker_version)
    st.write('Docker running:', sql.docker_is_running)
    if not sql.docker_is_running: 
        st.write("Docker is not running")
    st.write('Container running:', sql.container_is_running)

    if st.button("Restart the MySQL Container"):
        sql.stop_container()
        sql.start_container()

# Create a new database
query = st.chat_input("Enter your SQL query here:")
if query:
    with st.spinner(f"Running query: {query}"):
        result = sql.query(query)
        #result = sql.query("USE user;")
        #st.write(result)
        #result = sql.query("SHOW TABLES")
    with st.spinner("Updating the database summary"):
        with Databases: st.table(sql.get_summary())
        if query.strip().upper().startswith("USE"):
            print("The query starts with 'USE'.")
            st.table(sql.query("SHOW TABLES"))
        else:
            st.table(result)
    
#sql.close()
