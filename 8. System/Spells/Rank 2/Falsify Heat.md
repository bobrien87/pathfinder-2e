---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Illusion]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 willing creature or object"
duration: "8 hours"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You veil the signs of the fires of vitality, altering the target's apparent body temperature. This illusion applies to all senses, and a creature that touches the target can attempt to disbelieve the illusion. You can Dismiss the spell. Choose an illusory body temperature when you cast the spell.

- **Moderate** The target's body temperature appears the same as the surrounding environment, giving the target a +2 circumstance bonus to Deception checks to Impersonate an undead, a cold-blooded creature, or an inanimate object (such as a corpse). The target is also [[Invisible]] to heatvision and other abilities that sense heat similarly.

- **Warm** The target appears to emit substantial body heat, gaining a +2 circumstance bonus to Deception checks to Impersonate a warm-blooded creature.

**Heightened (4th)** You can target up to 10 creatures, and you can choose a different body temperature for each of them.

**Source:** `= this.source` (`= this.source-type`)
