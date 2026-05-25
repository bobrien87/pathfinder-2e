---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Air]]", "[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Nonlethal]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "20-foot burst"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call forth a swirling storm of dust. The *dust storm* obscures vision, with the effect of [[Mist]]. The dust also makes the air unbreathable; creatures in the area must hold their breath, though wearing a scarf or similar clothing over the mouth increases the time the creature can hold its breath to 5 rounds. Creatures entering or starting their turn in the *dust storm* take 1d6 slashing damage. Creatures that have the water trait or that are made primarily of liquid take double damage.

**Heightened (+2)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
