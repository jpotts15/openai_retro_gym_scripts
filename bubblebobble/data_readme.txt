#Variables found using the integration toolkit

#variable that changes with any x,y movement
{
  "info": {
    "all_movement": {
      "address": 515,
      "type": "=d2"
    },

#variable changes each time a bubble is blown, not exactly a +1 as the variable seems to store some position
    "bubble": {
      "address": 211,
      "type": "|u1"
    },

#tracks number of enemies on map
    "enemies": {
      "address": 1174,
      "type": "|u1"
    },

#tracks level you are on
    "level": {
      "address": 1025,
      "type": "|u1"
    },

#tracks your lives, game displays this value +1
    "lives": {
      "address": 46,
      "type": "|u1"
    },

#score, games shows this * 10
    "score": {
      "address": 56,
      "type": ">n6"
    },

#this is time tick that counts up, never explored when it resets or why
    "time_tick": {
      "address": 1118,
      "type": "<u4"
    },

#player x position, not perfect as its scaled/reprents map position in a unknown way
    "x": {
      "address": 515,
      "type": "|u1"
    },

#player y position, not perfect as its scaled/reprents map position in a unknown way
    "y": {
      "address": 516,
      "type": "|d1"
    }
  }
}
