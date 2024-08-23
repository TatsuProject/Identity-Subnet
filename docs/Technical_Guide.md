# Technical Guide

## System Requirements

| Items               | Required  | Recommended |
|---------------------|-----------|-------------|
| **CPU Physical Cores** | 4         | 8           |
| **CPU Speed**       | 2.5GHz     | 3.0GHz      |
| **RAM**             | 8GB        | 16GB        |
| **Storage**         | 10GB       | 50GB        |
| **Operating System** | Ubuntu 20.04 | Ubuntu 24.04 |
| **Bandwidth**       | 100Mbps/20Mbps | -        |

## Step-by-Step Guide to Running a Miner/Validator on Ta𝜏su Identity Subnet

To run a miner on the Ta𝜏su Identity Subnet using the instructions provided in the `running_on_testnet.md` file from the repository, follow these detailed steps:

### Prerequisites:

- Ensure you have Python installed (preferably version 3.7 or higher).
- Install Git for cloning the repository.
- Ensure you have a suitable text editor or IDE for editing configuration files.

### Steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Ta𝜏suProject/Identity-Subnet.git
    ```

    Navigate to the project directory:

    ```bash
    cd Identity-Subnet
    ```
    ![Screenshot 1](../assets/td1.jpg)
2. **Install Dependencies:** 

    Ensure you have pip installed, then install the necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```
    ![Screenshot 2](../assets/td2.jpg)
3. **Generate Wallet Keys:**

    To participate as a miner, you need to set up wallet keys. You can specify the name you want for the wallet:

    ```bash
    btcli wallet new_coldkey --wallet.name "NAME"
    ```
    ![Screenshot 3](../assets/td3.jpg)
    This will generate a new wallet and return the coldkey for that wallet. Remember to keep this key secure. Now create a hotkey for the wallet you just created:

    ```bash
    btcli wallet new_hotkey --wallet.name "NAME" --wallet.hotkey default
    ```
    ![Screenshot 4](../assets/td4.jpg)
    This command will generate a hotkey and coldkey for your miner wallet. Securely store the generated keys. And use any faucet to get Tao in your wallet.

4. **Register Keys**

    This step registers your subnet validator or subnet miner keys to the subnet.

    Register your miner key to the subnet:

    ```bash
    btcli subnet register --netuid 192 --subtensor.network test --wallet.name miner --wallet.hotkey default
    ```
    ![Screenshot 5](../assets/td5.jpg)

    ## OR
    Register your validator key to the subnet:

    ```bash
    btcli subnet register --netuid 192 --subtensor.network test --wallet.name validator --wallet.hotkey default
    ```
    ![Screenshot 6](../assets/td5.jpg)
    Follow the prompts:


5. **Run the Process:**

    Use the following command to start the miner:

    ```bash
    python neurons/miner.py --netuid 192 --subtensor.network test --wallet.name "NAME" --wallet.hotkey default --logging.debug
    ```
    ![Screenshot 7](../assets/td7.jpg)
    OR

    Use the following command to start the Validator:

    ```bash
    python neurons/validator.py --netuid 192 --subtensor.network test --wallet.name validator --wallet.hotkey default --logging.debug
    ```
    ![Screenshot 8](../assets/td8.jpg)
6. **Monitor and Verify:**

    - Monitor the console output to ensure the miner/validator is running correctly.
    - The logging information should help you verify that the miner is correctly processing data and communicating with the network.