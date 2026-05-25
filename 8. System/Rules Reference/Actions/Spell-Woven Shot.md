---
type: action
source-type: "Remaster"
cast: "`pf2:3`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You are wielding a loaded magic firearm or magic crossbow

**Effect** You Cast a Spell that takes 1 or 2 actions to cast and requires a spell attack roll. The effects of the spell do not occur immediately but are imbued into the required weapon. Make a Strike with that weapon. Your spell flies with the ammunition, using your attack roll result to determine the effects of both the Strike and the spell. This counts as two attacks for your multiple attack penalty, but you don't apply the penalty until after you've completed the Spell-Woven Shot.

**Source:** `= this.source` (`= this.source-type`)
