---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Attack]]", "[[Cold]]", "[[Concentrate]]", "[[Holy]]", "[[Light]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "1 creature"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You unleash a holy beam of freezing moonlight. Make a ranged spell attack. The ray deals 5d6 cold damage; if the target has the unholy trait, you deal an extra 5d6 spirit damage.

*Moonlight ray*'s cold damage is silver damage for the purposes of weaknesses, resistances, and the like.
- **Critical Success** The target takes double cold damage, as well as double spirit damage if a fiend or undead.
- **Success** The target takes full damage.

If the light passes through an area of magical darkness or targets a creature affected by magical darkness, *moonlight ray* attempts to counteract the darkness. If you need to determine whether the light passes through an area of darkness, draw a line between yourself and the spell's target.

**Heightened (+1)** The cold damage increases by 2d6, and the spirit damage against fiends and undead increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
