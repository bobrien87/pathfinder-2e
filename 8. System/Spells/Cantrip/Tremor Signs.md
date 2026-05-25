---
type: spell
sub-type: "Cantrip"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Earth]]", "[[Manipulate]]", "[[Subtle]]"]
cast: "`pf2:1`"
range: "120 feet"
targets: "1 creature"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You send a series of tremors, no longer than a short sentence of speech, toward your target. If the target is within range and connected to the same body of earth as you, the vibrations reach the target through the ground. You need neither line of sight nor line of effect, so a target on another floor of a building is a valid target.

The target can give a brief, vibrational response as a reaction, or as a free action on their next turn, but they must be within range to do so. If they respond, their response is delivered to you through tremors you feel, as with the original message. The tremors impart a clear meaning only if you and the target know that meaning, such as three tremors for a specific warning, two for another. Neither of you can impart a nuanced or new meaning using this spell.

A creature that has tremorsense can feel the vibrations from this spell if the creature is within range of the vibrations at any point during their journey to any target.

**Heightened (4th)** The spell can target up to 5 creatures.

**Source:** `= this.source` (`= this.source-type`)
