---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Plant]]", "[[Wood]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 willing creature"
duration: "10 minutes"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The target's skin becomes tough, with a consistency like bark or wood. The target gains resistance 2 to bludgeoning and piercing damage and weakness 3 to fire. After the target takes fire damage, it can Dismiss the spell as a free action triggered by taking the damage; doing so doesn't reduce the fire damage the target was dealt.

> [!danger] Effect: Spell Effect: Oaken Resilience

**Heightened (+2)** The resistances increase by 2, and the weakness increases by 3.

**Source:** `= this.source` (`= this.source-type`)
