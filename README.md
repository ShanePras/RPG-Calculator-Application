This project is currently a work in progress. It is made to be used as an application for Computer Role Playing to allow for battles to be simulated in a classic RPG setting. However, there are no set turn limits, and many MP costs can be modified in the settings menu. My goal is to make this a flexible and customizable interface, such that values can easily be modified for any kind of experience.\
\
Using Imports:\
Factor all character data in a csv file. There must be 18 columns, and do not include a title row. All columns must be ordered as the following:\
character Name, character Tag (used for commands), max HP, max MP, physical attack, range attack, defense, agility, luck, slice resist, strike resist, pierce resist, fire resist, water resist, lightning resist, earth resist, wind resist, other resist.\
Physical attack, range attack, and defense, are self explanatory. Agility controls chance to miss, but also chance to dodge. Luck controls chance of getting crits.\
All "resists" control what kinds of attacks characters can resist or not resist. 0-Normal, 1-Weak, 2-Resists, 3-Null, 4-Reflect, 5-Drain\
\
Current Goals:
- Finish Buff Menu
- Finish Heal Menu
- Add guard and charge functionality
- Add a character creator window to help with imports
