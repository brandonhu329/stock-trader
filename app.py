import streamlit as st

st.set_page_config(page_title="Stock Trader", layout="wide")

st.title("Stock Trader")
st.caption("Paper trading dashboard")

st.info("Preview only — market data and trading are not connected yet.")

symbol = st.text_input("Stock symbol", value="AAPL").strip().upper()

shares = st.number_input(
    "Number of shares",
    min_value=1,
    value=1,
    step=1
)

side = st.selectbox("Action", ["Buy", "Sell"])

if st.button("Preview order"):
    if not symbol:
        st.error("Enter a stock symbol.")
    else:
        st.write(f"{side} {shares} share(s) of {symbol}")
        st.caption("No order has been submitted.")