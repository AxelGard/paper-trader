# paper-trader

This is a python application that can trade on the stocks.

The application is using the [Alpaca API](https://alpaca.markets/) for trading.

[![Open this project in Cloud
Shell](http://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/AxelGard/paper-trader)

<div style="width:150px; height:100px">
<img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/Storck_Harbour_scene.jpg"
     width="500" height="600" alt="https://en.wikipedia.org/wiki/Trade#/media/File:Storck_Harbour_scene.jpg"
     style="float: left; margin-right: 10px;" />
</div>


## latest patch

the latest patch :

### randy random

the randy random update

<div style="width:150px; height:100px">
<img src="https://rimworldwiki.com/images/thumb/3/33/Randy.png/250px-Randy.png"
     width="250" height="300" style="float: left; margin-right: 10px;" />
</div>

With Randy random the application is able to buy and sell at random.
Why would we ever do this?
Due to that just like a cat picking who will win a bunch of football matches we might be able to do well at random.
There is still some things that need to be fixt in this patch.

The name Randy random comes from the game [RimWorld](https://store.steampowered.com/app/294100/RimWorld/).<br >
[Randy Random](https://rimworldwiki.com/wiki/Randy_Random), is a wild storyteller whose main characteristic is triggering challenges at any time of any difficulty, to the extent of launching several dangerous threats all at the same time or consecutively.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install

```
python 3
```

### Installing

Unix :

```
./install_requirements.sh
```

in the folder application there are a file that is called key.json
this file you will need to enter your key's for the Alpaca API

```
{
  "APCA-API-KEY-ID":"your_pub_key",
  "APCA-API-SECRET-KEY":"your_private_key"
}
```

you can now deploy

```
source env/bin/activate
./run_application.sh
```

### Coding style

the code style is using [pep8](https://pep8.org/)

## Deployment

for know you can just run the **run_application.sh** for deploying the program.

the file just runs the main.py file.

```
source env/bin/activate
./run_application.sh
```

## Built With

* [Python](https://www.python.org/) - language
* [Alpaca API](https://alpaca.markets/) - the trading api
* []() -

## Versioning

this code is just a side project i will some day make branch or tag with a stable release but for now there are not a stable version.

## Authors

* **Axel Gard** - *Initial work* - [AxelGard](https://github.com/AxelGard)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

<!-- https://cdn.dribbble.com/users/1186632/screenshots/4153391/camel.jpg -->

## Acknowledgments

* [alpaca API](https://alpaca.markets/)
*
*
