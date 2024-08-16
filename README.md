
# Microservice C - Probability Calculator

## Overview
This microservice calculates the probability of rolling a specific number with a given number of dice. It performs the calculation based on standard probability formulas and returns the result to the main application.

## Functionality
- Calculates probability for a given dice roll scenario.

## Communication
- **Protocol:** ZeroMQ (REP-REQ)
- **Port:** `tcp://*:5557`
- **Endpoints:**
  - Calculates the probability of rolling a specific number with a set of dice.

## Requirements
- ZeroMQ library.

## How to Run
1. Ensure ZeroMQ is installed.
2. Run the script using Python:
   ```bash
   python microservice_c.py
