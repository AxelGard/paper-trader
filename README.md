# paper-trader

This is a python application that can trade on the stocks.

The application is using the [Alpaca API](https://alpaca.markets/) for trading.

[![Open this project in Cloud
Shell](http://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/AxelGard/paper-trader)

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/AxelGard/paper-trader)

<div style="width:150px; height:100px">
<img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/Storck_Harbour_scene.jpg"
     width="500" height="600" alt="https://en.wikipedia.org/wiki/Trade#/media/File:Storck_Harbour_scene.jpg"
     style="float: left; margin-right: 10px;" />
</div>

Storck Harbour scene by Abraham Storck

## Versioning

latest version path note: 
### [v2.0 - alpaca lib](https://github.com/AxelGard/paper-trader/releases/tag/v2.0)
beawere that this verson needs python 3.5 or newer to work. v1.0 works with 3.4 or lower but not 2. 
In the second version realise of paper-trader I have introduced the official alpaca lib for python.
Because of this introduction of the library we are able to add a lot of new functions. 
I have moved the key file so you might need to move that if you are using a older version. 
There is also a lot of bug fixes in this version. 

this version is a **more stable version then v1.0** so if you have been using v1.0 you **should upgrade**

**[more](VERSIONS.md)**

## Traders

The names comes from the game [RimWorld](https://store.steampowered.com/app/294100/RimWorld/).

### Cassandra Classic

<div style="width:150px; height:100px">
<img src="https://rimworldwiki.com/images/thumb/9/9d/Cassandra.png/250px-Cassandra.png"
     width="250" height="300" style="float: left; margin-right: 10px;" />
</div>

my plan for Cassandra is to have a more Classical way of trading were it look to just make small profit buy remember what it bout at and then when made some profit sell.


### Phoebe Chillax

<div style="width:150px; height:100px">
<img src="https://rimworldwiki.com/images/thumb/3/35/Phoebe.png/250px-Phoebe.png"
     width="250" height="300" style="float: left; margin-right: 10px;" />
</div>

not clear

### randy random

<div style="width:150px; height:100px">
<img src="https://rimworldwiki.com/images/thumb/3/33/Randy.png/250px-Randy.png"
     width="250" height="300" style="float: left; margin-right: 10px;" />
</div>

[Randy Random](https://rimworldwiki.com/wiki/Randy_Random), is a wild storyteller whose main characteristic is triggering challenges at any time of any difficulty, to the extent of launching several dangerous threats all at the same time or consecutively.
With Randy random the application is able to buy and sell at random.
Why would we ever do this?
Due to that just like a cat picking who will win a bunch of football matches we might be able to do well at random.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install

```bash
python 3
```

### Installing

On macOS and Linux:

```bash
python3 -m venv env
source env/bin/activate
./install_requirements.sh
```

There are a file that is called **key.json**
this file you will need to enter your key's for the Alpaca API

```json
{
  "APCA-API-KEY-ID":"your_pub_key",
  "APCA-API-SECRET-KEY":"your_private_key"
}
```

you can now deploy

```bash
source env/bin/activate
./run_paper_trader.sh
```

### Coding style

the code style I am is using [pep8](https://pep8.org/).<br>
If you want to build you own trader there are a lot of basic functions in the [trader.py](src/traders/trader.py).<br>
So that you can build faster.

### File struct 
```
.
├── env
├── install_requirements.sh
├── key.json
├── LICENSE
├── README.md
├── requirements.txt
├── run_paper_trader.sh
├── src
│   ├── api_controller.py
│   ├── __init__.py
│   ├── main.py
│   ├── __pycache__
│   ├── test.py
│   └── traders
│       ├── cassandra_classic.py
│       ├── __init__.py
│       ├── lists
│       │   ├── stock_list_conservative.csv
│       │   ├── stock_list.csv
│       │   └── stock_list_long.csv
│       ├── log
│       │   ├── log.csv
│       │   └── log-info.md
│       ├── my_trader.py
│       ├── phoebe_chillax.py
│       ├── randy_random.py
│       ├── stockpickr.py
│       └── trader.py
└── VERSIONS.md

```


## Deployment

For now you can just run the **run_paper_trader.sh** for deploying the program.
the file just runs the main.py file.
If you have already ran source command you don't need to run it again.

```bash
source env/bin/activate
./run_paper_trader.sh
```

## Built With

* [Python](https://www.python.org/) - language
* [Alpaca API](https://alpaca.markets/) - the trading api
* [alpaca-trade-lib](https://github.com/alpacahq/alpaca-trade-api-python) - official trading-api lib

## Authors

* **Axel Gard** - *Initial work* - [AxelGard](https://github.com/AxelGard)

See also the list of [contributors](https://github.com/AxelGard/paper-trader/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

<!-- https://cdn.dribbble.com/users/1186632/screenshots/4153391/camel.jpg -->

## Acknowledgments

* [alpaca API](https://alpaca.markets/)
* [Rimworld](https://store.steampowered.com/app/294100/RimWorld/)
*



                                                                                  s                                ..
                                                                                 :8                              dF
     .d``                      .d``                       .u    .               .88       .u    .               '88bu.                    .u    .
     @8Ne.   .u         u      @8Ne.   .u        .u     .d88B :@8c             :888ooo  .d88B :@8c        u     '*88888bu        .u     .d88B :@8c
     %8888:u@88N     us888u.   %8888:u@88N    ud8888.  ="8888f8888r          -*8888888 ="8888f8888r    us888u.    ^"*8888N    ud8888.  ="8888f8888r
      `888I  888. .@88 "8888"   `888I  888. :888'8888.   4888>'88"             8888      4888>'88"  .@88 "8888"  beWE "888L :888'8888.   4888>'88"
       888I  888I 9888  9888     888I  888I d888 '88%"   4888> '               8888      4888> '    9888  9888   888E  888E d888 '88%"   4888> '
       888I  888I 9888  9888     888I  888I 8888.+"      4888>                 8888      4888>      9888  9888   888E  888E 8888.+"      4888>
     uW888L  888' 9888  9888   uW888L  888' 8888L       .d888L .+   88888888  .8888Lu=  .d888L .+   9888  9888   888E  888F 8888L       .d888L .+
    '*88888Nu88P  9888  9888  '*88888Nu88P  '8888c. .+  ^"8888*"    88888888  ^%888*    ^"8888*"    9888  9888  .888N..888  '8888c. .+  ^"8888*"
    ~ '88888F`    "888*""888" ~ '88888F`     "88888%       "Y"                  'Y"        "Y"      "888*""888"  `"888*""    "88888%       "Y"
       888 ^       ^Y"   ^Y'     888 ^         "YP'                                                  ^Y"   ^Y'      ""         "YP'
       *8E                       *8E
       '8>                       '8>
        "                         "
