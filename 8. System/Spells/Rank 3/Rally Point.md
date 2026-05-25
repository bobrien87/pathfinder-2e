---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Teleportation]]"]
cast: "`pf2:2`"
range: "touch"
area: "5-foot square"
duration: "1 minute"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You mark the area touched as a rally point. During the spell's duration, you can take a single action, which has the concentrate trait, to teleport to the rally point along with items you are wearing or holding. This teleportation fails if the area is occupied, if the rally point is more than 120 feet away, or if you try to bring along any other creature, even if it's in an extradimensional container. Once you teleport to the rally point, the spell's duration ends.

**Heightened (7th)** You can designate up to four other creatures within 30 feet, in addition to yourself. Each of these creatures can teleport to the rally point once during the spell's duration by taking a single action, which has the concentrate trait. The spell's duration no longer ends once you teleport to the rally point, though you still can't teleport to the rally point again.

**Source:** `= this.source` (`= this.source-type`)
