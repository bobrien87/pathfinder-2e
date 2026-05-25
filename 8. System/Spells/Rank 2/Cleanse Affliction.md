---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Healing]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 willing creature"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Gentle restorative magic pushes back the effects of toxins and more complex maladies. Choose an affliction on the target, such as a curse, disease, or poison. If it has advanced past stage one, reduce the stage by one. This reduction can be applied only once to a given case of an affliction, with the case ending when it's completely cured. Although the reduction can't occur again, heightened versions of this spell attempt to counteract with each casting.

**Heightened (3rd)** Attempt to counteract the affliction if it is a disease or poison.

**Heightened (4th)** Attempt to counteract the affliction if it is a curse, disease, or poison.

**Source:** `= this.source` (`= this.source-type`)
