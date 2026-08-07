import streamlit as st
import requests

# INFORMATION OF PRIVATE
GITHUB_USER = "INVYZERO"
REPO_NAME = "visa-itinerary-system-core"
TOKEN = st.secrets["GH_TOKEN"]

@st.cache_resource
def fetch_core_code():
    url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/app.py"
    headers = {"Authorization": f"token {TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        st.error(f"❌ Không thể kết nối kho lõi (Lỗi: {response.status_code})")
        st.stop()

# Tải code thật về và chạy trực tiếp trên RAM của máy chủ
core_code = fetch_core_code()
exec(core_code)
