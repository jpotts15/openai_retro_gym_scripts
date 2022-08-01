{
  "crop": [
    0,
    0,
    0,
    0
  ],
  
  #for the done condition I set it to lives = 0 as well as a y position that reads out on the end game screen
  #this ensures that the last life/other things that happen while the lives variable is set is counted correctly as a reward
  
  "done": {
    "condition": "all",
    "nodes": {
      "subnodeName": {
        "variables": {
          "y": {
            "op": "equal",
            "reference": 54
          }
        }
      }
    },
    "variables": {
      "lives": {
        "op": "equal"
      }
    }
  },
  #last setup for this, i've tried to scale rewards in a way that AI will move around, blow bubbles and kill enemies while avoiding getting killed
  #still imperfect but for most AI algos it produces the desired results
  #some AIs will not work very well with the negative incentive on lives so testing is always necessary to find right balance
  "reward": {
    "variables": {
      "all_movement": {
        "reward": 9.999999747378752e-05
      },
      "bubble": {
        "reward": 0.009999999776482582
      },
      "enemies": {
        "penalty": -20.0
      },
      "level": {
        "reward": 40.0
      },
      "lives": {
        "penalty": 40.0
      },
      "score": {
        "reward": 0.10000000149011612
      },
      "x": {
        "reward": 0.009999999776482582
      },
      "y": {
        "reward": 0.0010000000474974513
      }
    }
  }
}
