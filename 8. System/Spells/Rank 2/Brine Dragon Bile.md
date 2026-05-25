---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Acid]]", "[[Attack]]", "[[Concentrate]]", "[[Water]]"]
cast: "`pf2:r`"
range: "30 feet"
targets: "the creature that took damage"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** A creature within range takes damage from a slashing or piercing attack, or one that inflicts persistent bleed damage.

You spit a glob of caustic saltwater that stings the wounds of the creature. Make a ranged spell attack against the triggering creature's AC. On a hit, salt scours its open wound, dealing 2d6 persistent acid damage.

**Heightened (+2)** The persistent damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
