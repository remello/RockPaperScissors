

# Rock-Paper-Scissors

Playable Rock-Paper-Scissors game, with a Player vs Computer mode. Practice using arrays, the Random library, formatted strings, and algorithms.

## About

StackEdit stores your files in your browser, which means all your files are automatically saved locally and are accessible **offline!**

## How to use

 1. Firstly, enter your name. If you played this game before, it would load your previous score 
 2. Next, you can input your options split by commas e.g.: `rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire` If you want to play a standard game, just press Return
 4. The program will automatically identify which option beats which.
 5. To check your score use `!rating`
 6. To save and exit, use `!exit`


## Relationships between different options

Firstly, every option is equal to itself (causing a draw if both the user and the computer choose the same option). Secondly, every option wins over one-half of the other options of the list and gets defeated by another half.  The program finds the option for which it wants to know relationships with other options.  

 - It takes all the options that follow this chosen option in the list and adds them to the list of options that precede the chosen option.

- Now we have another list of options that don't include the "chosen" option and has a different order of elements in it (first go the options following the chosen one in the original list, after they are the ones that precede it). So, in this "new" list, the first half of the options will be defeating the "chosen" option, and the second half will get beaten by it.

For example, the user's list of options is `rock,paper,scissors,lizard,spock`. You want to know what options are weaker than `lizard`. By looking at the list `spock,rock,paper,scissors` you realize that `spock` and `rock` will be beating the `lizard`, and `paper` and `scissors` will get defeated by it. For spock it'll be almost the same, but it'll get beaten by `rock` and `paper`, and prevail over `scissors` and `lizard`. For the version of the game with 15 options, you can look at the picture above to understand the relationships between options.
