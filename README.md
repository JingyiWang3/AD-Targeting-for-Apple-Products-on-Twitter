# E6893-Big-Data-Project

import data into MongoDB Atlas (cloud):

`mongoimport --host Cluster0-shard-0/cluster0-shard-00-00-5mcg4.mongodb.net:27017,cluster0-shard-00-01-5mcg4.mongodb.net:27017,cluster0-shard-00-02-5mcg4.mongodb.net:27017 --ssl --username yh2866 --password Aa123456 --authenticationDatabase admin --db donorschoose --collection projects --type csv --headerline --file data.csv`

it must run by:

`python3 app.py `

import data into mongodb (local):

`mongoimport -d donorschoose -c projects --type csv --headerline /PATH/TO/DATA/data.csv`
