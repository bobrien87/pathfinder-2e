---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Illusion]]", "[[Manipulate]]", "[[Subtle]]", "[[Visual]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "10-foot burst"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a cloud of mesmerizing patterns and colors that hovers in the air. Creatures are [[Dazzled]] while inside the cloud. In addition, a creature must attempt a Will saving throw if it is inside the cloud when you cast it, when it enters the cloud, when it ends its turn within the cloud, or if it uses a [[Seek]] or Interact action on the cloud. A creature currently [[Fascinated]] by hypnotize doesn't attempt new saves.
- **Success** The target is unaffected.
- **Failure** The target is fascinated by the cloud.
- **Critical Failure** The target is fascinated by the cloud. While it remains fascinated, it can't use reactions.

**Source:** `= this.source` (`= this.source-type`)
