
<!-- TOC -->

- [Introduction](#introduction)
- [PyFolio](#pyfolio)
- [Interactive Brokers Python API IB API](#interactive-brokers-python-api-ib-api)
- [QuantStats](#quantstats)
- [Backtrader](#backtrader)
- [OpenBB SDK](#openbb-sdk)
- [RiskFolio-Lib](#riskfolio-lib)

<!-- /TOC -->


# Introduction

This file is based on Jason Strimpel newsletter

# PyFolio

pyfolio is a Python library for performance and risk analysis of financial portfolios that works well with the Zipline open-source backtesting library.

At the core of pyfolio are various tear sheets that combine various individual plots and summary statistics to provide a comprehensive view of the performance of a trading algorithm.

These tear sheets present performance and risk metrics for a backtest separately during the backtest and out-of-sample periods.

In addition, it visualizes how several risk and return metrics behave over time.

pyfolio is no longer officially maintained by Quantopian which dissolved in 2020.

Stefan Jansen now actively maintains pyfolio under the repo called pyfolio-reloaded.

Dive deeper: https://pyfolio.ml4trading.io​



# Interactive Brokers Python API (IB API)

The TWS API is a simple yet powerful interface through which IB clients can automate trading strategies, request market data, monitor account balances, and portfolios in real-time.

The API is designed to automate some of the operations you would normally perform manually within TWS such as placing orders, monitoring your account balance and positions, or viewing an instrument's live data.

There is no logic within the API other than to ensure the integrity of the exchanged messages.

Most validations and checks occur in the backend of TWS and IB's servers.

Because of this, it is highly convenient to familiarize yourself with the TWS itself to understand how the platform works.

Dive deeper: https://interactivebrokers.github.io/tws-api/​



# QuantStats

QuantStats performs portfolio profiling, allowing quants and portfolio managers to understand their performance better by providing them with in-depth analytics and risk metrics.

QuantStats has a statistics module for calculating various performance metrics of a trading strategy or backtest, and a plotting module for visualizing those metrics over time.

It has a reports module for generating metrics reports, batch plotting, and creating tear sheets that can be saved as an HTML file.

QuantStats plays nicely with the output of many backtesting frameworks.

Dive deeper: https://github.com/ranaroussi/quantstats​


# Backtrader

Backtrader is a popular, Python-based, event-driven backtest framework.

It lets you spend more time focusing on writing reusable trading strategies, models, signals, and analysis and less time building the infrastructure.

Another nice feature of Backtrader is that it connects to Interactive Brokers for live data and trading.

You can also import your own custom data through CSV.

It comes with built-in indicators using the popular TA-Lib library. Backtrader has reusable analyzers for returns over time, Sharpe ratio, and volatility.

The results output plays nice with QuantStats, too.

his is a powerful combination that lets you avoid writing the code from scratch.

Dive deeper: https://github.com/mementum/backtrader​


# OpenBB SDK

The OpenBB SDK gives you programmatic access to the capabilities of the OpenBB Terminal.

You have the building blocks to create your own financial tools and application—whether it be a visualization dashboard or a custom report on Jupyter Notebook.

You get access to normalized financial data from dozens of data providers without having to develop your own integrations from scratch.

On top of financial data feeds, OpenBB SDK also provides you with a toolbox to perform financial analysis on a variety of asset classes, including stocks, crypto, ETFs, funds, and the economy.

Dive deeper: https://openbb.co/​


# RiskFolio-Lib

Riskfolio-Lib is a library for making quantitative strategic asset allocation or portfolio optimization in Python.

It helps practitioners build investment portfolios based on mathematically complex models with low effort.

It is built on top of cvxpy and closely integrated with pandas DataFrames.

Riskfolio-Lib helps with portfolio optimization using mean-variance, risk parity portfolio, clustering, worst case, Black Litterman, and dozens of others.