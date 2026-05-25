---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Spirit]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 ally and 1 enemy"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You entreat a spirit or the spiritual energies in your location to surround and protect an ally from an certain foe. Each time the enemy attacks and damages the ally, the enemy takes 1d6 spirit damage. The enemy is aware of these spirits and has a general sense that attacking the ally will draw the spirits' ire.

**Heightened (+2)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
