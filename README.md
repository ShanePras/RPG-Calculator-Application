This project is currently a work in progress. It is made to be used as an application for Computer Role Playing to allow for battles to be simulated in a classic RPG setting. However, there are no set turn limits, and many MP costs can be modified in the settings menu. My goal is to make this a flexible and customizable interface, such that values can easily be modified for any kind of experience.\
\
Using Imports:\
Factor all character data in a csv file. There must be 18 columns, and do not include a title row. All columns must be ordered as the following:\
character Name, character Tag (used for commands), max HP, max MP, physical attack, range attack, defense, agility, luck, slice resist, strike resist, pierce resist, fire resist, water resist, lightning resist, earth resist, wind resist, other resist.\
\
Physical attack, range attack, and defense, are self explanatory. Agility controls chance to miss, but also chance to dodge. Luck controls chance of getting crits.\
\
All "resists" control what kinds of attacks characters can resist or not resist. \
- 0-Normal
- 1-Weak
- 2-Resists
- 3-Null
- 4-Reflect
- 5-Drain\
\
Status: \
- Burn: Extra 10% MaxHP dmg when attacked (auto)
- Frostbite: 2x chance to get critical striked (auto)
- Shock: Damage output reduced by 30% (auto)
- Heavy: Unable to dodge, defense increase by 10% (auto)
- Daze: Dodge chance cut in half. (auto)
- Curse: Unable to be healed/buffed (auto)
- Poison: 10% MaxHP damage after an action (manual, use debug menu to do this)
- Charm: Attacks allies or buffs/heals enemies (manual)
- Confusion: 50% chance to ignore commands (manual)
- Forget: Restricted to basic attacks, guards, or items (manual)
- Rage: Forced basic attacks (manual). Increased damaged by 20%, decrease defense by 60% (auto)
- Fear: May ignore commands (manual), agility reduced by 40% (auto). 
Current Goals: \
- Finish Element Break/Wall Menu
- Add a character creator window to help with imports
