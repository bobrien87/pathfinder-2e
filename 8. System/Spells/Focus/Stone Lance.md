---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Earth]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "1 creature"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure a jagged lance of stone and then launch it at a foe. Make a spell attack roll against the target. On a hit, you deal 6d6 piercing damage and the lance impales the creature, giving it a –10-foot circumstance penalty to its Speeds unless it Escapes. On a critical hit, if the creature is on the ground, the lance also embeds into the ground and [[Immobilizes]] the creature until it Escapes. A creature that Escapes after being impaled takes 3 bleed damage. When the spell ends, the lance crumbles into dirt, freeing the target if it hasn't Escaped.

**Heightened (+1)** Increase the damage by 2d6 and the persistent bleed damage for Escapes by 1.

**Source:** `= this.source` (`= this.source-type`)
