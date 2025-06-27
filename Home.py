import streamlit as st

st.set_page_config(page_title="DynamoDB show full table")

# CSS
def apply_local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

apply_local_css("styles.css")

from aws_client   import create_session, get_dynamodb_table
from data_fetcher import scan_table, count_records
from pathlib import Path
import boto3, botocore

# ── UI header

VERSION = "0.1.0"
st.markdown(f"<p style='font-size: 0.9rem; color: #6b7280;'>🔧 version {VERSION}</p>", unsafe_allow_html=True)

# ── Login / Logout
with st.form("aws_login"):
    st.subheader("AWS Login")
    aid  = st.text_input("AWS Access Key ID",  value=st.session_state.get("aws_access_key_id", ""))
    sak  = st.text_input("AWS Secret Access Key", type="password", value=st.session_state.get("aws_secret_access_key", ""))
    tok  = st.text_input("Session Token (optional)", type="password", value=st.session_state.get("aws_session_token", ""))
    reg  = st.text_input("Region", value=st.session_state.get("region_name", "eu-central-1"))
    c1, c2 = st.columns(2)
    login  = c1.form_submit_button("🔌 Login")
    logout = c2.form_submit_button("🔒 Logout")

if login:
    try:
        boto3.client("sts", region_name=reg,
                     aws_access_key_id=aid, aws_secret_access_key=sak,
                     aws_session_token=tok or None).get_caller_identity()
        st.session_state.aws_creds = dict(
            aws_access_key_id=aid, aws_secret_access_key=sak,
            aws_session_token=tok or None, region_name=reg)
        st.session_state.update({"aws_access_key_id": aid,
                                 "aws_secret_access_key": sak,
                                 "aws_session_token": tok,
                                 "region_name": reg})
        st.success("Connected ✅")
    except botocore.exceptions.ClientError as e:
        st.error(e)

if logout:
    for k in ("aws_creds", "available_tables", "df"):
        st.session_state.pop(k, None)
    st.success("Logged out")

# ── rest only if logged-in
if "aws_creds" not in st.session_state:
    st.stop()

st.session_state.setdefault("available_tables", [])
creds = st.session_state.aws_creds
region = creds["region_name"]

# fetch tables
if st.button("🔍 Fetch Table List"):
    try:
        session = create_session(**creds)
        st.session_state.available_tables = session.client("dynamodb").list_tables()["TableNames"]
        st.success(f"Tables: {len(st.session_state.available_tables)}")
    except Exception as e:
        st.error(e)

table = st.selectbox("Table", st.session_state.available_tables or ["(no tables)"])

c1, c2, c3 = st.columns(3)
if c1.button("👁️ Show"):
    try:
        df = scan_table(get_dynamodb_table(create_session(**creds), table))
        st.session_state.df = df
        st.dataframe(df)
    except Exception as e:
        st.error(e)

if c2.button("🔄 Refresh"):
    if "df" in st.session_state and st.session_state.df is not None:
        try:
            df = scan_table(get_dynamodb_table(create_session(**creds), table))
            st.session_state.df = df
            st.dataframe(df)
        except Exception as e:
            st.error(e)

if c3.button("🔢 Count"):
    try:
        total = count_records(get_dynamodb_table(create_session(**creds), table))
        st.info(f"Total: {total}")
    except Exception as e:
        st.error(e)
