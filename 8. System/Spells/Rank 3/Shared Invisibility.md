---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Aura]]", "[[Illusion]]", "[[Manipulate]]", "[[Subtle]]"]
cast: "`pf2:2`"
area: "30-foot emanation"
targets: "you and up to 5 willing creatures"
duration: "10 minutes"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You and all targets are [[Invisible]] except to each other as long as the targets remain within the emanation. If a creature made invisible by this spell leaves the spell's area, it becomes visible and remains so even if it returns to the spell's area. If any creature made invisible by this spell uses a hostile action, the spell ends after the hostile action is completed.

**Heightened (5th)** The targets increase to you and up to 10 willing creatures. The duration increases to 1 hour.

**Source:** `= this.source` (`= this.source-type`)
