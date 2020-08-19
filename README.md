# Nector
Multi-exchange API wrapper 🦏🔓🐝

<img src="img/cover.jpeg" align="center" />

## Setup & usage

- pip3 install git+https://github.com/quan-digital/nector#egg=nector



#### Public topics subscribed

```bash
"chat",                // Trollbox chat - cummulative push
"instrument",          // Instrument updates including turnover and bid/ask - continuous push overwrite 
"liquidation",         // Liquidation orders as they are entered into the book - push refreshed after 20 seconds
"quoteBin1m",          // 1-minute quote bins - cummulative push
"tradeBin1m",          // 1-minute trade bins - cummulative push
```
