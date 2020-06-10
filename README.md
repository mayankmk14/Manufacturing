# Car Supply Chain

HYPERLEDGER Sawtooth - Car Supply Chain Transaction Processor Demo

1. To create an account on Blockchain using an Admin
2. PartFactory - can register its parts on BC.
3. PartFactory - will transafer ownership to CarFactory.
4. CarFactory - Create car using assigned parts.
5. CarFactory - will transafer ownership to Dealer.

Each Asset Can be tracked using the Trails Structure after mapping events emitted

Sawtooth v1.1(poet-simulator)

Docker v19.03.1

Using Poet-Simulator as consensus (Smartcontract remains unchanged) to create a multi-validator(3) network

Commands :
To start Blockchain (from root folder) : `docker-compose up`