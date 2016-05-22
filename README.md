# RankMyPlace

##URL: 

## Intro
This project is an example of what you can extract from open data of a city.
The choosen city is Lyon - France.

![Alt text](/ScreenShots/HomePage.png?raw=true)

RankMyPlace is divided in four services described bellow

### Techs:
* Python 3
* Angular.js

## Services

### Mark an address

First you have to choose your profile : Student, Family, Young active people, Senior or custom

You can customize your profile with the criterias by saying how important it is for you.

After that you have to type your address.

Then you have your global mark !

On the bottom of the page you have some details on two tabs.
* For each criteria you have the satisfaction (or insatisfaction) based on your profile.
* For each criteria you have the criteria marked objectively.

![Alt text](/ScreenShots/1.png?raw=true)

### Comparison between profiles at a specific address

This service is similar to the previous one but you can't use custom profiles.

You just type your address and you have the comparison of profiles at this address with the same interface than the previous service.

![Alt text](/ScreenShots/2.png?raw=true)

### Find bests addresses for your profile

This service show you a heatmap wich represents bests adresses for your profile.

![Alt text](/ScreenShots/3.png?raw=true)

### Find zones with a lack of services according to criterias

Here you choose a zone and a criteria and you'll see where this criteria has the best mark

![Alt text](/ScreenShots/4.png?raw=true)
## API

All calculations are done on back-end, you can request the API easily on 6 routes:
* GET /profiles
* GET /criterias
* POST /ranking
* GET /heatmap
* GET /heatmap/{grid_basename}/{criteria_name}
* POST /heatmap/{grid_basename}

### About

Forked from https://github.com/Hexanonyme/PLD_SmartCity

contact : Gazolike@gmail.com