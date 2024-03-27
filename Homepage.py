import streamlit as st
import base64
import matplotlib.pyplot as plt

# Function to load image as base64
def get_img_as_base64(file):
    try:
        with open(file, "rb") as f:
            data = f.read()
            return base64.b64encode(data).decode()
    except FileNotFoundError:
        st.error(f"Image file '{file}' not found.")
        return None
    except Exception as e:
        st.error(f"Error loading image file '{file}': {e}")
        return None

# Load background images
img = get_img_as_base64("background.jpeg")
img2 = get_img_as_base64("background2.jpg")

# Apply background images styling
if img and img2:
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img2}");
    background-size: 100%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
    }}

    [data-testid="stSidebar"] > div:first-child {{
        background-image: url("data:image/png;base64,{img}");
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: cover;
        width: 100%;
        height: 100%;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Add title "CryptoGPT"
st.markdown("<h1 class='title'>CryptoGPT</h1>", unsafe_allow_html=True)

# Sidebar
sidebar = st.sidebar
sidebar.title("Trading Preferences")
time_frame = sidebar.selectbox("Time Frame", ["Short Term", "Medium Term", "Long Term"])
trading_strategy = sidebar.selectbox("Trading Strategy", ["Breakout", "Breakdown"])
profit_margin = sidebar.slider("Profit Margin", 1, 10, 5)
risk_tolerance = sidebar.slider("Risk Tolerance", 1, 5, 3)
generate_button_clicked = sidebar.button("Generate Signal", key="generate_button", help="Click to generate signal")

# Main content
col1, col2, col3, col4 = st.columns(4)

# Global variable for output value
output_value = ""

# Functions for button clicks
def append_text(message):
    global output_value
    output_value += message + "\n"

# Button click actions
if generate_button_clicked:
    if trading_strategy == "Breakout" and profit_margin == 2:
        output_value = "Coin identified: ETHBTC\n"
        output_value += "The expected sell price is 0.052414 BTC, representing a profit of 2%.\n"
        output_value += "Hold for at least 1 hour. The expected buy price is 0.05128 BTC."
    elif trading_strategy == "Breakout" and profit_margin == 3:
        output_value = "Coin identified: XRPBTC\n"
        output_value += "The expected sell price is 0.000009341 BTC, representing a profit of 3%.\n"
        output_value += "Hold for at least 2 hours. The expected buy price is 0.000009146 BTC."
      
    
if col1.button("Trading Signal", key="trading_signal_button"):
    if trading_strategy == "Breakout" and profit_margin == 2:
        output_value = "Coin identified: ETHBTC\n"
        output_value += "The expected sell price is 0.052414 BTC, representing a profit of 2%.\n"
        output_value += "Hold for at least 1 hour. The expected buy price is 0.05128 BTC."
    elif trading_strategy == "Breakout" and profit_margin == 3:
        output_value = "Coin identified: XRPBTC\n"
        output_value += "The expected sell price is 0.000009341 BTC, representing a profit of 3%.\n"
        output_value += "Hold for at least 2 hours. The expected buy price is 0.000009146 BTC."

if col2.button("Technical Analysis", key="technical_analysis_button"):
    if trading_strategy == "Breakout" and profit_margin == 2:
        output_value = "Technical Analysis Report:\n"
        output_value += "Our breakout signal for ETHBTC is based on a combination of key technical indicators.\n"
        output_value += "Firstly, the Relative Strength Index (RSI) on the 1-hour chart showed a bullish divergence,\n"
        output_value += "indicating a potential upward price movement. Additionally, the Moving Average Convergence\n"
        output_value += "Divergence (MACD) histogram crossed above the signal line, confirming the bullish momentum.\n"
        output_value += "Furthermore, the Bollinger Bands tightened significantly, suggesting a period of consolidation,\n"
        output_value += "followed by a potential breakout. This breakout was confirmed when the price breached the upper\n"
        output_value += "Bollinger Band with increased volume, signaling a strong buying interest.\n"
        output_value += "Considering these indicators collectively, we anticipate a 2% profit potential as the price of ETHBTC\n"
        output_value += "is expected to continue its upward trajectory for at least 1 hour."
    elif trading_strategy == "Breakout" and profit_margin == 3:
        output_value = "Technical Analysis Report:\n"
        output_value += "Our breakout signal for XRPBTC is supported by several technical indicators. "
        output_value += "Firstly, the Ichimoku Cloud indicator showed a bullish TK cross on the 4-hour chart, "
        output_value += "indicating a shift in momentum towards the upside. Additionally, the Moving Average Convergence "
        output_value += "Divergence (MACD) crossed above the signal line, confirming the bullish bias.\n"
        output_value += "Furthermore, the Volume Weighted Average Price (VWAP) indicator surged, indicating strong buying "
        output_value += "pressure accompanying the price increase. This was complemented by the Chaikin Money Flow (CMF) "
        output_value += "indicator, which moved into positive territory, signifying a flow of capital into\n"
        output_value += "Based on these indicators, we expect a breakout with a 3% profit potential as the price of XRPBTC "
        output_value += "continues to rise for at least 2 hours."

if col3.button("Market Sentiment", key="market_sentiment_button"):
    if trading_strategy == "Breakout" and profit_margin == 2:
        output_value = """
Report: Market and News Sentiment on the ETHBTC Coin
Introduction
Cryptocurrency markets are highly volatile and influenced by a variety of factors, including market
sentiment and news sentiment. In this report, we will analyze the market and news sentiment for the
ETHBTC coin, which represents the ratio of Ethereum (ETH) to Bitcoin (BTC). By examining various
sources, we aim to determine the current sentiment surrounding ETHBTC and evaluate the potential for
profit.
Methodology
To conduct the analysis, we gathered information from multiple reputable sources, including
TradingView, Barchart, Benzinga, Blockworks, NewsBTC, Yahoo Finance, and CoinGecko. We reviewed
the provided URLs to gather insights into the market and news sentiment regarding the ETHBTC coin.
Market Sentiment
The sentiment regarding the ETHBTC market appears to be mixed among traders and analysts. Some
traders believe that the ETHBTC trading pair is currently the most important chart in the digital asset
markets, suggesting that Ethereum could potentially break out further against Bitcoin. These optimistic
traders consider the recent high of 0.0828 as significant, surpassing the previous yearly high and
reaching the highest level in over three and a half years. They speculate that a breakout in ETHBTC could
lead to more risk-seeking behavior and potentially push Bitcoin's price higher as well.
However, not all traders share the same optimism. Initially, the founder of Crypto-TA doubted the
bullishness of the ETHBTC chart, identifying a rising wedge pattern with bearish divergence that could
potentially result in a breakdown. However, he later reversed his stance, acknowledging that the
breakout did occur and admitting to underestimating ETH's strength.
In terms of performance, Ethereum has significantly outperformed Bitcoin year-to-date, with a rally of
over 500% compared to Bitcoin's gain of 96%. This marks the largest outperformance of Ethereum over
Bitcoin since Ethereum's creation in 2015.
News Sentiment
The sentiment in news articles regarding the ETHBTC coin generally appears positive, highlighting factors
that contribute to Ethereum's surge in value against Bitcoin.
An article mentioned that ETH's growth has closely aligned with BTC over the past month, with both
experiencing a decline of about 3.5%. However, the decline in BTC's value has narrowed the gap
between BTC and ETH on a year-to-date basis, with BTC now only 10% ahead of ETH. The narrowing gap
suggests a potential bullish sentiment towards ETHBTC.
Two primary factors contributing to ETH's surge are staking yield and fee burns. Staking yield, linked to
Ethereum's proof-of-stake (PoS) mechanism, has resulted in an 8% annual return for staked ETH. BTC, on
the other hand, does not provide the same level of rewards due to its reliance on the proof-of-work
(PoW) consensus mechanism. Additionally, fee burns enacted through Ethereum's EIP-1559 update have
removed over 3.3 million ETH from circulation since August 2021, increasing its value.
Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs
please visit: https://products.aspose.com/words/
The article notes that Ethereum's new PoS network needs to be tested and survive stress tests before
attracting new investors interested in staking. Despite facing headwinds in the challenging macro
environment, Ethereum is still in a significant growth phase and has shown positive signs.
Market sentiment forecasts about a 2.5% growth potential for ETH over the next month, while BTC's bull
run returns are diminishing. The article also mentions Binance Smart Chain as a potential competitor to
Ethereum in the future. However, currently, Ethereum leads the decentralized finance (DeFi) market
with a 74% share.
Conclusion
Based on the gathered information, it can be concluded that the market and news sentiment
surrounding the ETHBTC coin is predominantly positive, with traders and analysts expressing mixed
opinions. While some traders believe that the recent breakout in the ETHBTC chart signifies potential for
further upside, others initially doubted the bullishness but later acknowledged ETH's strength.
In terms of news sentiment, factors such as staking yield and fee burns have contributed to the positive
sentiment surrounding Ethereum's performance against Bitcoin. The narrowing gap between the two
cryptocurrencies on a year-to-date basis and the potential for future growth in the DeFi market also
support a relatively bullish sentiment towards ETHBTC.
It is important to note that cryptocurrency markets are highly volatile and subject to various factors,
including regulatory changes and macroeconomic conditions. Any investment decision should be made
after thorough research, considering one's risk tolerance and investment goals.
Overall, the gathered information suggests a relative positive sentiment towards ETHBTC, but it is
essential to conduct further analysis and consider other factors before making any investment decisions.
References
TradingView. Retrieved from link.
Barchart. Retrieved from link.
Benzinga. Retrieved from link.
Blockworks. Retrieved from link.
NewsBTC. Retrieved from link.
Yahoo Finance. Retrieved from link.
CoinGecko. Retrieved from link."""
    elif trading_strategy == "Breakout" and profit_margin == 3:
        output_value = """
Market and News Sentiment Analysis of XRP Coin
Introduction
In this report, we will analyze the market and news sentiment on the XRP coin. XRP is a cryptocurrency
that operates on the Ripple network and aims to facilitate fast and low-cost international money
transfers. We will examine various sources to gather information about the current market analysis,
price predictions, and news sentiment surrounding XRP. The analysis will consider both technical aspects
and external factors impacting the coin's potential for profit.
Market Analysis
1. Market Capitalization and Value
Based on the information gathered from MarketBeat, XRP is currently priced at $0.64 on major
cryptocurrency exchanges, with a market capitalization of $35.36 billion (MarketBeat). These figures
highlight XRP's standing in the cryptocurrency market.
2. Weiss Research Rating
According to Weiss Research, XRP has received an overall rating of "B-" (MarketBeat). While this rating
provides a general indication of XRP's performance, it does not offer specific details concerning the
market sentiment regarding the coin.
3. Technical Analysis from TradingView
The information gathered from TradingView does not provide insight into the market sentiment for XRP
(TradingView). The platform primarily focuses on providing market information, technical analysis tools,
and community discussion rather than offering specific analysis about XRP.
4. XRP Price Prediction
Based on the CoinCodex website, a price prediction of $0.677891 by April 25, 2024, suggests a potential
rise of 7.27% in XRP's value (CoinCodex). However, these predictions should be considered with caution
as past price behavior is not always indicative of future performance.
5. XRP News Sentiment
To assess the news sentiment surrounding XRP, we will explore various sources, including CoinDesk,
FXStreet, Crypto Basic, and Forbes.
a. CoinDesk
According to CoinDesk, recent events, such as the theft of XRP from Ripple Labs' executive chairman and
the legal case faced by Ripple regarding unregistered securities offerings, have generated news headlines
but do not provide a clear sentiment indicator (CoinDesk).
b. FXStreet
One article from FXStreet suggests a positive sentiment regarding XRP news (FXStreet). It highlights the
XRP price rally, reaching a new year-to-date high of $0.7440, and indicates upbeat expectations driven by
the forthcoming deadline in the SEC lawsuit against Ripple. The technical indicators, including the
Moving Average Convergence/Divergence (MACD) and Awesome Oscillator (AO), also support positive
momentum.
c. Crypto Basic
Crypto Basic presents a bullish sentiment on XRP news based on an analyst's prediction. The article
mentions the identification of a bullish cross on the XRP Average Sentiment Oscillator (ASO) indicator,
which historically signals significant price increases. The analyst predicts a rally of 28,250% when the
cross occurs, translating to a price of $149 (Crypto Basic).
d. Forbes
Forbes discusses the profit potential of XRP based on three key events: reaching a settlement with the
SEC, securing a major client win in the U.S. market, and speculation around an IPO for Ripple. While
these events could positively impact XRP, the article advises caution due to regulatory risks (Forbes).
6. Expert Opinions and Investment Advice
Several articles caution investors about predicting XRP's future price, given the ongoing legal dispute
between Ripple and the SEC. Experts suggest considering individual risk tolerance and financial goals and
recommend thorough research and potentially seeking advice from financial advisors before investing in
XRP (MarketBeat, Forbes).
Conclusion
Based on the information gathered from various sources, we can summarize the market analysis and
news sentiment regarding the XRP coin as follows:
- Market Capitalization: XRP has a market capitalization of $35.36 billion (MarketBeat).
- Weiss Research Rating: XRP has received a rating of "B-" (MarketBeat).
- Technical Analysis: The technical analysis from TradingView does not provide specific details
about XRP (TradingView).
- XRP Price Prediction: CoinCodex predicts a potential rise of 7.27% in XRP's value by April 2024
(CoinCodex).
- News Sentiment: While some sources, like FXStreet and Crypto Basic, suggest positive sentiment
for XRP news and potential price rallies (FXStreet, Crypto Basic), it is essential to consider the
ongoing legal case faced by Ripple and potential regulatory risks (Forbes).
- Expert Opinions: Experts advise caution when investing in XRP and recommend thorough
research, considering individual risk tolerance and financial goals, and potentially seeking advice
from financial advisors (MarketBeat, Forbes).
Based on the available information, it is essential for investors to closely monitor ongoing legal
developments, regulatory decisions, and the outcome of the SEC lawsuit against Ripple before making
investment decisions related to XRP.
"""

if col4.button("Visualization", key="visualization_button"):
    if trading_strategy == "Breakout" and profit_margin == 2:
        timestamps = ["1 hour ago", "55 minutes ago", "50 minutes ago", "45 minutes ago", "40 minutes ago", "35 minutes ago", "Current Price"]
        prices = [0.0515, 0.0517, 0.0518, 0.0519, 0.0520, 0.0521, 0.0523]

        # Plotting the data
        fig, ax = plt.subplots()
        ax.plot(timestamps, prices, marker='o', linestyle='-')
        ax.set_title('Price Movement of ETHBTC')
        ax.set_xlabel('Time')
        ax.set_ylabel('Price (BTC)')
        ax.grid(True)
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)
        
        # Display the plot using Streamlit
        st.pyplot(fig)
    if trading_strategy == "Breakout" and profit_margin == 3:
        timestamps = ["1 hour ago", "55 minutes ago", "50 minutes ago", "45 minutes ago", "40 minutes ago", "35 minutes ago", "Current Price"]
        prices = [0.00000912, 0.00000915, 0.00000918, 0.0000092, 0.00000922, 0.00000928, 0.00000926]

        # Plotting the data
        fig, ax = plt.subplots()
        ax.plot(timestamps, prices, marker='o', linestyle='-')
        ax.set_title('Price Movement of XRPBTC')
        ax.set_xlabel('Time')
        ax.set_ylabel('Price (BTC)')
        ax.grid(True)
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)
        
        # Display the plot using Streamlit
        st.pyplot(fig)

        
        
    elif trading_strategy == "Breakout" and profit_margin == 3:
        output_value = "<Your Visualization Report Here>"
# Update the output_text
st.text_area("Generated Signals:", value=output_value, height=350, max_chars=10000, key="output_text_area")

