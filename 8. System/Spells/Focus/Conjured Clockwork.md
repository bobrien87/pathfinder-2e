---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Wizard]]"]
cast: "`pf2:2`"
range: "60 feet"
area: "10-foot burst"
defense: "basic Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder #215: To Blot Out the Sun"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure a complex clockwork device on the ground and cause it to slowly spread across the battlefield. The area is difficult terrain. Each creature that enters or ends its turn in the area takes 2d8 slashing damage with a basic Reflex save. A creature can take this damage only once per turn. On subsequent rounds, the first time you Sustain the spell each round, you can expand the radius of the clockwork device by 5 feet.

**Heightened (+2)** The damage increases by 1d8.

**Source:** `= this.source` (`= this.source-type`)
