---
type: action
source-type: "Remaster"
traits: ["[[Fortune]]"]
cast: "`pf2:2`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Effect** You make a Strike with a ranged weapon, rolling the attack and damage twice and using the better results for each. The attack ignores circumstance penalties to the attack roll and any flat check required due to the target being [[Concealed]] or [[Hidden]].

**Source:** `= this.source` (`= this.source-type`)
