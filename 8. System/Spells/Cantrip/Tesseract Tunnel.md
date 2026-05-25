---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Manipulate]]", "[[Psychic]]", "[[Teleportation]]"]
cast: "`pf2:2`"
duration: "1 minute (sustained)"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You race from point to point, tearing open a tunnel in space. You create a portal in your current space and then Stride, creating another portal in the space you end your [[Stride]]. Until the beginning of your next turn, any creature that enters the first portal can immediately transport itself to the exit portal as part of its move action, which adds the teleportation trait to its movement.

You can have only one *tesseract tunnel* open at a time; creating another causes the first to immediately close. You can use *tesseract tunnel* while [[Burrowing]], [[Climbing]], [[Flying]], or [[Swimming]] instead of Striding if you have the corresponding movement type.

**Source:** `= this.source` (`= this.source-type`)
