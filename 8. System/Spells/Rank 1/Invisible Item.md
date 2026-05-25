---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 object"
duration: "1 hour"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You make the object [[Invisible]]. This makes it [[Undetected]] to all creatures, though the creatures can attempt to find the target, making it [[Hidden]] to them instead if they succeed. If the item is used as part of a hostile action, the spell ends after that hostile action is completed. Making a weapon invisible typically doesn't give any advantage to the attack, except that an invisible thrown weapon or piece of ammunition can be used for an attack without necessarily giving information about the attacker's hiding place unless the weapon returns to the attacker.

**Heightened (3rd)** The duration is until the next time you make your daily preparations.

**Heightened (7th)** The duration is unlimited.

**Source:** `= this.source` (`= this.source-type`)
