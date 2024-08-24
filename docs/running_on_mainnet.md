# Running Subnet on Mainnet

This tutorial shows how to use the bittensor `btcli` to connect your miner/validator to Tatsu Identity. 

**IMPORTANT:** Before attempting to register on mainnet, we strongly recommend that you:
- First run [Running Subnet Locally](running_on_staging.md), and
- Then run [Running on the Testnet](running_on_testnet.md).

**DANGER**
- Do not expose your private keys.
- Only use your testnet wallet.
- Do not reuse the password of your mainnet wallet.
- Make sure your incentive mechanism is resistant to abuse. 

## Prerequisites

Before proceeding further, make sure that you have installed Bittensor. See the below instructions:

- [Install `bittensor`](https://github.com/opentensor/bittensor#install).

After installing `bittensor`, proceed as below:

## Steps

## 1. Install Tatsu Identity subnet template

**NOTE: Skip this step if** you already did this during local testing and development.

In your project directory:

```bash
git clone https://github.com/TatsuProject/Identity-Subnet.git 
```

Next, `cd` into `Identity-Subnet` repo directory:

```bash
cd Identity-Subnet
```

Install the Bittensor subnet template package:

```bash
python -m pip install -e .
pip install -r requirements.txt
```

## 2. Create wallets 

Create wallets for subnet validator and/or for subnet miner.
  
This step creates local coldkey and hotkey pairs for your identity: subnet validator and/or subnet miner. 

The validator and miner will be registered to the subnet created by the owner. This ensures that the validator and miner can run the respective validator and miner scripts.

**NOTE**: You can also use existing wallets to register. Creating new keys is shown here for reference.

Create a coldkey for the wallet:

```bash
btcli wallet new_coldkey --wallet.name miner
```

and

```bash
btcli wallet new_hotkey --wallet.name miner --wallet.hotkey default
```



The above command will show:

```bash
>> Subnet lock cost: τ100.000000000
```

## 3. Register keys 


This step registers your subnet validator and/or subnet miner keys to the subnet giving them the repective slots on the subnet.

Register your key to the subnet:

```bash
btcli subnet recycle_register --netuid 38 --subtensor.network finney --wallet.name miner --wallet.hotkey default
```

Follow the below prompts:

```bash
>> Enter netuid [1]: #Enter 38 as Tatsu Identity is registered at netuid 38
>> Continue Registration?
  hotkey:     ...
  coldkey:    ...
  network:    finney [y/n]: # Select yes (y)
>> ✅ Registered
```

## 4. Check that your keys have been registered

Check that your key has been registered:


```bash
btcli wallet overview --wallet.name miner 
```

The output will be similar to the below:

```bash
Subnet: 1                                                                                                                                                                
COLDKEY  HOTKEY   UID  ACTIVE  STAKE(τ)     RANK    TRUST  CONSENSUS  INCENTIVE  DIVIDENDS  EMISSION(ρ)   VTRUST  VPERMIT  UPDATED  AXON  HOTKEY_SS58                    
miner    default  1      True   0.00000  0.00000  0.00000    0.00000    0.00000    0.00000            0  0.00000                14  none  5GTFrsEQfvTsh3WjiEVFeKzFTc2xcf…
1        1        2            τ0.00000  0.00000  0.00000    0.00000    0.00000    0.00000           ρ0  0.00000                                                         
                                                                          Wallet balance: τ0.0   
```

## 5. Run subnet miner and subnet validator

Run the subnet miner:

```bash
python neurons/miner.py --netuid 38  --wallet.name miner --wallet.hotkey default --logging.debug
```

You will see the below terminal output:

```bash
>> 2023-08-08 16:58:11.223 |       INFO       | Running miner for subnet: 1 on network: wss://entrypoint-finney.opentensor.ai:443 with config: ...
```

#OR

Run the subnet validator:

```bash
python neurons/validator.py --netuid 38  --wallet.name validator --wallet.hotkey default --logging.debug
```

You will see the below terminal output:

```bash
>> 2023-08-08 16:58:11.223 |       INFO       | Running validator for subnet: 1 on network: wss://entrypoint-finney.opentensor.ai:443 with config: ...
```


## 6. Stopping your nodes

To stop your nodes, press CTRL + C in the terminal where the nodes are running.

---
