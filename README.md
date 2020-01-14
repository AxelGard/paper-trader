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

### [v2.0 - coming soon](https://github.com/AxelGard/paper-trader/releases/tag/v1.0)

I will be releasing version v2.0 soon in v2.0 the major change from v1.0 is that in v2.0 I have used the alpaca library for python.
With that library I was able to add a lot of new features and fix bugs.
Of curse you can already find most of v2.0 in the master branch.
I have been testing the new version but soon it will be ready.
I am still running the old version on my main server for trading,
but when the new version is relist I will also move that server to v2.0.
This also means that will be retiring the old version more or less,
so you should use v2.0 when it's has been released. 

### [v1.0 - first version](https://github.com/AxelGard/paper-trader/releases/tag/v1.0)

The first version of the paper-trader.
This version of the paper-trader uses the alpaca REST API over https.
In v1.0, I used python requests for sending orders.

**be aware that this version has some problems and should not be used for professional trading.**

feel free to use but at your own risk


## Traders

The names comes from the game [RimWorld](https://store.steampowered.com/app/294100/RimWorld/).<br >
[Randy Random](https://rimworldwiki.com/wiki/Randy_Random), is a wild storyteller whose main characteristic is triggering challenges at any time of any difficulty, to the extent of launching several dangerous threats all at the same time or consecutively.

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

the code style is using [pep8](https://pep8.org/)

## Deployment

for know you can just run the **run_paper_trader.sh** for deploying the program.
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
