---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Illusion]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
area: "5-foot burst"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a brief vision of immense wealth filling the spell's area. Each creature within 20 feet of the area that could be enticed by material wealth must attempt a Will saving throw. A creature that enters the area automatically disbelieves the illusion, and disbelieving the illusion ends any [[Fascinated]] condition imposed by the spell. As long as you Sustain the Spell, other creatures react to the treasure like they would any other illusion, but they are not at risk of becoming Fascinated.
- **Critical Success** The creature disbelieves the illusion and is unaffected by it.
- **Success** The creature is Fascinated by the wealth until it has completed its first action on its next turn.
- **Failure** The creature is Fascinated by the illusion.

**Source:** `= this.source` (`= this.source-type`)
