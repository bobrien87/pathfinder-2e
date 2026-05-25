---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "6"
traits: ["[[Mythic]]"]
cast: "8 hours"
range: "touch"
targets: "1 physical structure"
duration: "14 days"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You protect a physical structure from the devastation caused by immense creatures. This structure can be artificially constructed, like a castle or wall, or a natural subject, like a specific tree or grove. A given casting of this ritual can protect a subject as small as a single-story house and no larger than the wall surrounding a large city.
- **Critical Success** As success, but the target structure also doubles its Hit Points and Broken Threshold.
- **Success** The target structure gains a +4 status bonus to AC and its Hardness increases by 10. It also gains resistance 20 to acid, cold, electricity, fire, and sonic damage; this resistance applies before its Hardness. These benefits apply only to attacks made by Gargantuan creatures or siege engines.
- **Failure** The ritual doesn't succeed.
- **Critical Failure** The target is considerably weakened, reducing its Hardness by 10 (minimum 0).

**Source:** `= this.source` (`= this.source-type`)
