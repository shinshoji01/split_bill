# Split Bill
You can split bill with your friends. Please edit csv file as illustrated in `csv/`.

# Docker Environment
This repository contains docker environment to allow anyone to try my model. To make the execution simple, I created my environment with docker-compose. Please follow the procedure below to build my environment.

1. Go to `Docker/`
2. `docker-compose up -d`
3. `docker-compose exec split_bill python3 split_bill.py {csv file}`
  - For example: `docker-compose exec split_bill python3 split_bill.py csv/20211119_rental_space.xlsx`
