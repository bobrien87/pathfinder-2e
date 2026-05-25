---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Force]]", "[[Manipulate]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You surround yourself in a vortex of whirling colorful scarves of force that obfuscate you and disorient your foes. You gain the benefits of the [[Concealed]] condition, but only against ranged and melee attacks. When a melee attack fails to hit you because of the flat check for the concealed condition, the scarves snag the weapon or unarmed attack, and the creature takes a –1 circumstance penalty to further attacks with that weapon or unarmed attack until the end of its turn (or the end of its next turn, if it wasn't the creature's turn). The timing of the scarves' movement is harder to predict for ranged attackers, so the flat check for the concealed condition against ranged attacks increases from DC 5 to DC 6. You can Dismiss this spell.

**Heightened (+2)** The circumstance penalty to further attacks with a melee weapon or unarmed attack the scarves snag increases by 1. The DC of the flat check for the concealed condition against ranged attacks increases by 1.

**Source:** `= this.source` (`= this.source-type`)
