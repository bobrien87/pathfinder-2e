---
type: action
source-type: "Remaster"
cast: "`pf2:3`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're wielding your bonded beast gun or another magic firearm

**Effect** You Cast a Spell that takes 1 or 2 actions to cast and requires a spell attack roll. The effects of the spell do not occur immediately but are imbued into the beast gun you're wielding. Make a Strike with that beast gun. Your spell flies with the ammunition, using your attack roll result to determine the effects of both the Strike and the spell. Combine the Strike and spell's damage for the purpose of resistances and weaknesses. This counts as two attacks for the purposes of determining your multiple attack penalty, but you don't apply the penalty until after you've completed resolving the attack and spell.

**Special** If you also have the [[Spell Woven Shot]] action you can load and activate a piece of magical ammunition as a free action before making a Spellsling attack once per 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
