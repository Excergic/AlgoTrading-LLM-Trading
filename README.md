# AlgoTrading-LLM-Trading  

This project is trading framwwork which replicates dynamics of real world trading system.

![system-design](https://raw.githubusercontent.com/Excergic/images/main/allm-trading-systrem-design.png)  

## Trading Agent Role Specializations 

### Analyst Team  

- **Fundamental Analysts**: Assess company fundamentals to identify undervalued or overvalued stocks.  
- **Sentiment Analysts**: Analyze social media and public sentiment to gauge market mood.  
- **News Analysts**: Evaluate news and macroeconomic indicators to predict market movements.  
- **Technical Analysts**: Use technical indicators to forecast price trends and trading opportunities.    

### Researcher Team 

The Researcher Team critically evaluates analyst data through a dialectical process involving bullish and bearish perspectives. This debate ensures balanced analysis, identifying both opportunities and risks to inform trading strategies.  

- **Bullish Researchers**: Highlight positive market indicators and growth potential.  
- **Bearish Researchers**: Focus on risks and negative market signals.  

### Trader Agents  

Trader Agents execute decisions based on comprehensive analyses. They evaluate insights from analysts and researchers to determine optimal trading actions, balancing returns and risks in a dynamic market environment.  

- Assessing analyst and researcher recommendations.  
- Determining trade timing and size.  
- Executing buy/sell orders.  
- Adjusting portfolios in response to market changes.    

Precision and strategic thinking are essential for their role in maximizing performance.    

### Risk Management Team  

The Risk Management Team oversees the firm's exposure to market risks, ensuring trading activities stay within predefined limits.  

- Assessing market volatility and liquidity.  
- Implementing risk mitigation strategies.  
- Advising Trader Agents on risk exposures.  
- Aligning portfolio with risk tolerance.  
- They ensure financial stability and safeguard assets through effective risk control.  

All agents utilize the ReAct prompting framework, facilitating a collaborative and dynamic decision-making process reflective of real-world trading systems.  

## TradingAgents: Agent Workflow  

### Communication Protocol   

To enhance communication efficiency, **TradingAgents** employs a structured protocol that combines clear, structured outputs with natural language dialogue. This approach minimizes information loss and maintains context over long interactions, ensuring focused and effective communication among agents.  

### Types of Agent Interactions  

Unlike previous frameworks that rely heavily on unstructured dialogue, our agents communicate through structured reports and diagrams, preserving essential information and enabling direct queries from the global state.  

- **Analyst Team**: Compiles research into concise analysis reports.
- **Traders**: Review analyst reports and produce decision signals with detailed rationales.  

Natural language dialogue is reserved for specific interactions, such as debates within the Researcher and Risk Management teams, fostering deeper reasoning and balanced decision-making.

- **Researcher Team**: Engages in debates to form balanced perspectives.
- **Risk Management Team**: Deliberates on trading plans from multiple risk perspectives.
- **Fund Manager**: Reviews and approves risk-adjusted trading decisions.  

## Experiments  

We evaluated TradingAgents using a comprehensive experimental setup to assess its performance against various baselines.  

### Back Trading  

Our simulation utilized a multi-asset, multi-modal financial dataset including historical stock prices, news articles, social media sentiments, insider transactions, financial reports, and technical indicators from January to March 2024.  

### Simulation Setup  

The trading environment spanned from June to November 2024. Agents operated on a daily basis, making decisions based on available data without future information, ensuring unbiased results.  

### Baseline Models  

We compared **TradingAgents** against the following strategies:  

- **Buy and Hold**: Investing equally across selected stocks throughout the period.  
- **MACD**: Momentum strategy based on MACD crossovers.  
- **KDJ & RSI**: Combined momentum indicators for trading signals.  
- **ZMR**: Mean reversion strategy based on price deviations.  
- **SMA**: Trend-following strategy using moving average crossovers.  





