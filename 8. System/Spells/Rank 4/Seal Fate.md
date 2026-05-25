---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Death]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 living creature"
defense: "Fortitude"
duration: "varies"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You utter a curse that a creature will meet a certain end—a death by freezing, stabbing, or another means you devise. Choose one type of damage from the following list: acid, bludgeoning, cold, electricity, fire, piercing, slashing, sonic, or void. The effect is based on the target's Fortitude save.
- **Critical Success** The target is unaffected.
- **Success** The target gains weakness 2 to the chosen damage type until the end of your next turn.
- **Failure** As success, but the duration is 1 minute. If the creature is reduced to 0 Hit Points by the chosen damage and its level is 7 or less, it dies.
- **Critical Failure** As failure, but the duration is unlimited.

**Heightened (+2)** The weakness increases by 1, and the maximum level of creature that can be automatically killed increases by 4.

> [!danger] Effect: Spell Effect: Seal Fate

**Source:** `= this.source` (`= this.source-type`)
