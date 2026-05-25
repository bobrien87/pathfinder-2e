---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Air]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "500 feet"
area: "20-foot burst"
defense: "Fortitude"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Air pressure drops precipitously, causing pain and debilitation in creatures' inner ears and joints. Each living creature in the area of the spell when you cast it or that enters the area during the spell's duration must attempt a Fortitude save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Deafened]] and [[Clumsy]] 1 until the end of its next turn, after which it's temporarily immune for 1 hour.
- **Failure** The creature is deafened and [[Clumsy]] 2. At the end of each of its turns, it can attempt a new save if it's no longer in the pressure zone. On a success, it ends the effects and is temporarily immune for 1 hour.
- **Critical Failure** The creature is deafened and clumsy 2 for the duration of the spell.

A creature [[Deafened]] by this spell can attempt to end the condition by popping its ears. It can use a single action to attempt a new Fortitude save, losing the deafened condition from this spell on a success. Some creatures with anatomies that lack inner ears or joints might be immune to these effects, as determined by the GM.

**Source:** `= this.source` (`= this.source-type`)
