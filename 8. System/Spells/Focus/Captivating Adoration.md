---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Aura]]", "[[Cleric]]", "[[Concentrate]]", "[[Emotion]]", "[[Focus]]", "[[Manipulate]]", "[[Mental]]", "[[Visual]]"]
cast: "`pf2:2`"
area: "15-foot emanation"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You become intensely entrancing, and creatures are distracted by you as long as they remain within the area. You can exclude any creatures you choose from the effects. If a creature is in the aura when you Cast the Spell or when a creature enters the area for the first time, it must attempt a Will saving throw. If a creature leaves and reenters, it uses the results of its original save.
- **Critical Success** The creature is unaffected and temporarily immune for 1 hour.
- **Success** The creature is [[Fascinated]] with you for its next action, then is temporarily immune for 1 hour.
- **Failure** The creature is Fascinated with you.
- **Critical Failure** The creature is Fascinated with you, and its attitude toward you improves by one step.

**Heightened (+1)** Increase the size of the emanation by 15 feet.

**Source:** `= this.source` (`= this.source-type`)
