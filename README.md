
# Identity Subnet

The Identity Subnet project aims to calculate a human score based on various metrics such as GitHub account, Ethereum balance, Tao balance, Tao staked, and other relevant data points. The project involves validators and miners working together to compute and verify these scores.
Update: We are live on Testnet SN#192. For testing purposes, miners and validators can be connected to the subnet on SN192

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview 

The Identity Subnet uses a decentralized approach to calculate a human score for individuals based on several data points. Validators collect data from profiles and other sources, providing this data to miners. Miners then compute a human score and return it to the validator. The validator calculates its own score and matches it with the scores given by the miners. Miners with matching scores receive reward points.

## Features

- **Decentralized Data Collection:** Validators gather data from various profiles and metrics.
- **Human Score Calculation:** Miners calculate human scores based on provided data.
- **Score Verification:** Validators verify the accuracy of the scores calculated by miners.
- **Reward System:** Miners with accurate scores receive rewards.

## Architecture

The system consists of two main components:

1. **Validators:**
   - Collect data from profiles and other metrics.
   - Provide collected data to miners.
   - Calculate their own scores and verify miners' scores.

2. **Miners:**
   - Receive data from validators.
   - Calculate human scores.
   - Return scores to validators for verification.

## Installation

To set up the Identity Subnet project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/TatsuProject/Identity-Subnet.git
   cd Identity-Subnet
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables as needed (refer to `docs/running_on_testnet.md` for detailed instructions).

## Usage

To run the project, use the following commands (assuming that you have done the setup as decribed in docs):

1. Start the validator:
   ```bash
   python neurons/validator.py --netuid 192 --subtensor.network test --wallet.name miner --wallet.hotkey default --logging.debug
   ```

2. Start the miner:
   ```bash
   python neurons/miner.py --netuid 192 --subtensor.network test --wallet.name miner --wallet.hotkey default --logging.debug
   ```

For detailed usage instructions and examples, refer to the [documentation](docs/).

## Technical Guide

You can find the detailed Technical Guide in the docs folder, refer to [Technical_Guide](docs/Technical_Guide.md)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
