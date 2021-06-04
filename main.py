# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import streamlit as st


# %%
coin1 =np.array([[1, 15, 41, 60, 59, 90, 72, 63, 52, 70, 100, 156],[1, 20, 30, 60, 49, 69, 49, 10, 90, 140, 300, 140]])
data1 =pd.DataFrame(coin1, index=["CoinA", "CoinB"]).T
data1.head()


# %%
plot =sb.lineplot(data=data1, palette="magma",markers=True)
st.pyplot()


# %%
st.title("Crypto-currency value")
coin =st.selectbox("choose the coin :", list(["CoinA", "CoinB"]))
date =st.slider("choose the month :", min_value=0, max_value=12, value=5, step=1)
tell =st.button("See Value")

# %%
if tell:
    st.text(f"value => {list(data1[str(coin)])[date]}")
    st.pyplot(plot)

# %%
