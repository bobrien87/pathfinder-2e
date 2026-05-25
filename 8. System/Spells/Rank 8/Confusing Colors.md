---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Illusion]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Subtle]]", "[[Visual]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "20-foot burst"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A cloud of cascading, ever-changing colors manifests in the air. Creatures are [[Dazzled]] while inside the cloud, as are those within 20 feet of the cloud's area. A creature must attempt a Will save if it is inside the cloud when you cast it, enters the cloud, ends its turn within the cloud, or uses a [[Seek]] or Interact action on the cloud. A creature currently affected by the cloud doesn't need to attempt new saves.
- **Success** The creature is unaffected.
- **Failure** The creature is [[Confused]] for 1d4 rounds.
- **Critical Failure** The creature is [[Stunned]] for 1d4 rounds. After the stunned condition ends, the creature is confused for the remaining duration of the spell.

**Source:** `= this.source` (`= this.source-type`)
