---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Manipulate]]", "[[Plant]]", "[[Wood]]"]
cast: "`pf2:2`"
range: "100"
targets: "1 creature"
source: "Pathfinder #203: Shepherd of Decay"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You launch a curved length of wood at a foe that arcs around objects and obstacles to strike from an unexpected direction. Make a spell attack roll against the target's AC. This attack ignores the target's [[Concealed]] condition and ignores all cover except greater cover. If you hit, the projectile deals 7d10 bludgeoning damage.

**Heightened (7th)** The damage increases to 9d10.

**Heightened (9th)** The damage increases to 12d10, and the attack ignores cover completely.

**Source:** `= this.source` (`= this.source-type`)
