---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Focus]]", "[[Manipulate]]", "[[Morph]]", "[[Wizard]]"]
cast: "`pf2:1`"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You change your body to better suit the moment. You gain one of the following abilities of your choice. You can Dismiss this spell.

- You gain a 20-foot status bonus to your Speed.

- You gain a climb or swim Speed equal to half your Speed.

- You gain darkvision.

- You gain a pair of claws. These are agile finesse unarmed attacks that deal 1d8 slashing damage.

- You gain scent 60 feet (imprecise).

> [!danger] Effect: Spell Effect: Shifting Form

**Source:** `= this.source` (`= this.source-type`)
