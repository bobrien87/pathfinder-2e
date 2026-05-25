---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Manipulate]]", "[[Sonic]]"]
cast: "`pf2:3`"
range: "1,000 feet"
area: "30-foot burst"
defense: "Reflex"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

With a pinch of metallic powder and gunpowder, you call forth blistering red energy that shoots straight upward into the air and explodes, unleashing a crackling boom. Over time, you might even customize your own pattern and color for the skyrocket as you refine the spell.

You can't change the direction or distance of the rocket-it must go straight up, continuing up to the maximum range if possible. If the rocket explodes at its maximum height, the bright light can be seen up to 10 miles away, and the sound of the explosion can be heard up to 1 mile away under clear weather conditions.

If the rocket explodes in an enclosed space smaller than the full size of the burst, each creature in the area takes 1d10 sonic damage depending on the result of its Reflex save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is [[Dazzled]] for 1 round.
- **Critical Failure** The creature takes double damage and is [[Blinded]] for 1 round.

**Heightened (+1)** The sonic damage increases by 1d10.

**Source:** `= this.source` (`= this.source-type`)
