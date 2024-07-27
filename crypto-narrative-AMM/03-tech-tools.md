<!-- TOC -->

- [General frameworks and libraries](#general-frameworks-and-libraries)
  - [Libraries and Frameworks](#libraries-and-frameworks)
  - [Open-Source AMM Projects](#open-source-amm-projects)
  - [Tools and Resources](#tools-and-resources)
- [Liblararies and frameworks for market making](#liblararies-and-frameworks-for-market-making)
  - [Python Libraries](#python-libraries)
  - [Multi-Language Libraries](#multi-language-libraries)
- [For market making bots](#for-market-making-bots)
  - [**Superalgos**](#superalgos)
  - [**Jesse**](#jesse)
  - [**Hummingbot**](#hummingbot)

<!-- /TOC -->

## General frameworks and libraries

### Libraries and Frameworks

1. **OpenZeppelin**:

   - **Description**: OpenZeppelin provides secure and tested smart contract libraries that you can use to build your AMM. They offer a wide range of contracts for tokens, governance, and more.
   - **Repository**: [OpenZeppelin Contracts](https://github.com/OpenZeppelin/openzeppelin-contracts)
   - **Documentation**: [OpenZeppelin Docs](https://docs.openzeppelin.com/)

2. **web3.js**:

   - **Description**: This is a JavaScript library that allows you to interact with the Ethereum blockchain. It can be used for tasks like deploying contracts, interacting with smart contracts, and managing wallets.
   - **Repository**: [web3.js](https://github.com/ethereum/web3.js/)
   - **Documentation**: [Web3.js Docs](https://web3js.readthedocs.io/)

3. **Ethers.js**:
   - **Description**: Ethers.js is a library for interacting with the Ethereum blockchain and its ecosystem. It is lightweight and focuses on simplicity and ease of use.
   - **Repository**: [Ethers.js](https://github.com/ethers-io/ethers.js/)
   - **Documentation**: [Ethers.js Docs](https://docs.ethers.io/v5/)

### Open-Source AMM Projects

1. **Uniswap**:

   - **Description**: Uniswap is one of the most popular AMM protocols. Its V2 and V3 versions are open-source, providing a great starting point for understanding AMM mechanics and implementation.
   - **Repository**: [Uniswap V2](https://github.com/Uniswap/uniswap-v2-core), [Uniswap V3](https://github.com/Uniswap/uniswap-v3-core)
   - **Documentation**: [Uniswap Docs](https://docs.uniswap.org/)

2. **Balancer**:

   - **Description**: Balancer is another well-known AMM that supports multi-token pools with custom weights. It’s useful for more complex AMM designs.
   - **Repository**: [Balancer V2](https://github.com/balancer-labs/balancer-v2-monorepo)
   - **Documentation**: [Balancer Docs](https://docs.balancer.fi/)

3. **Curve Finance**:

   - **Description**: Curve is an AMM optimized for stablecoin trading, providing low slippage and low fee trades. Its codebase can be insightful for building AMMs that handle similar use cases.
   - **Repository**: [Curve Finance](https://github.com/curvefi/curve-contract)
   - **Documentation**: [Curve Docs](https://resources.curve.fi/)

4. **SushiSwap**:
   - **Description**: SushiSwap started as a fork of Uniswap but has developed its own unique features. The repository includes implementations for a variety of DeFi products, including AMM.
   - **Repository**: [SushiSwap](https://github.com/sushiswap/sushiswap)
   - **Documentation**: [SushiSwap Docs](https://docs.sushi.com/)

### Tools and Resources

1. **Hardhat**:

   - **Description**: Hardhat is a development environment to compile, deploy, test, and debug your Ethereum software. It's particularly useful for complex projects and debugging.
   - **Repository**: [Hardhat](https://github.com/nomiclabs/hardhat)
   - **Documentation**: [Hardhat Docs](https://hardhat.org/getting-started/)

2. **Chainlink**:
   - **Description**: Chainlink provides decentralized oracle networks that can bring off-chain data into your AMM smart contracts. This can be useful for price feeds and other data inputs.
   - **Repository**: [Chainlink](https://github.com/smartcontractkit/chainlink)
   - **Documentation**: [Chainlink Docs](https://docs.chain.link/)

## Liblararies and frameworks for market making

### Python Libraries

1. **CCXT (CryptoCurrency eXchange Trading)**

   - **Description**: CCXT is a library that abstracts away the differences between individual cryptocurrency exchange APIs, providing a unified interface. It supports more than 120 exchanges and can be used in Python, JavaScript, and PHP.
   - **Repository**: [CCXT on GitHub](https://github.com/ccxt/ccxt)

2. **Freqtrade**
   - **Description**: Freqtrade is a cryptocurrency trading library that supports many exchanges and includes features for backtesting, plotting, machine learning, and performance reporting. It also offers integration with Telegram for bot control.
   - **Repository**: [Freqtrade on GitHub](https://github.com/freqtrade/freqtrade)

### Multi-Language Libraries

1. **HftBacktest**
   - **Description**: A high-frequency trading and market-making backtesting tool in Python and Rust, designed for accurate market replay-based backtesting using full order book and trade tick feed data.
   - **Repository**: [HftBacktest on GitHub](https://github.com/nkaz001/hftbacktest)

## For market making bots

### **Superalgos**

- **Description**: Superalgos is a platform for designing, testing, and deploying crypto trading bots. It combines a visual scripting interface with powerful backtesting and execution capabilities.
- **Key Features**:
  - Visual strategy designer.
  - Multi-exchange support.
  - Comprehensive backtesting environment.
  - Community-driven with extensive documentation.
- **Repository**: [Superalgos on GitHub](https://github.com/Superalgos/Superalgos)

### **Jesse**

- **Description**: Jesse is an advanced crypto trading framework written in Python. It focuses on simplicity and ease of use for research and live trading.
- **Key Features**:
  - Easy-to-use API.
  - Real-time data streaming.
  - Advanced backtesting capabilities.
  - Multiple strategies support.
- **Repository**: [Jesse on GitHub](https://github.com/jesse-ai/jesse)

### **Hummingbot**

- **Description**: Hummingbot is an open-source platform that allows you to build and run high-frequency trading bots that automate trading on cryptocurrency exchanges.
- **Key Features**:
  - Supports multiple cryptocurrency exchanges.
  - Customizable strategies.
  - Backtesting and live trading.
  - Integration with liquidity mining campaigns.
- **Repository**: [Hummingbot on GitHub](https://github.com/hummingbot/hummingbot)
