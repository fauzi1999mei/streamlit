import streamlit as st 
from datetime import date 
import yfinance
from plotly import graph_objs as go 

START = '2015-01-01' 
TODAY = date.today().strftime('%Y-%m-%d')

st.title("Stock Prediction")
stocks =('goog', 'aapl', 'msft','gme') 
selected_stock = st.selectbox('select stock', stocks) 

n_years = st.slider('years of predictions : ', 1,4) 
period = n_years * 365

@st.cache 
def load_data(stock):
    data = yfinance.download(stock, START, TODAY) 
    data.reset_index(inplace=True) 
    return data

data = load_data(selected_stock) 

st.subheader('stock data') 
st.write('head')
st.write(data.head())
st.write('tail')
st.write(data.tail())

fig1 = go.Figure() 
fig1.add_trace(go.Scatter(x=data['Date'], y = data['Open'], name='stock_open'))
fig1.add_trace(go.Scatter(x=data['Date'], y = data['Close'], name='stock_close')) 
fig1.layout.update(title_text = 'time series data', xaxis_rangeslider_visible = True) 
st.plotly_chart(fig1) 
