---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "10"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "1 hour"
range: "5 feet"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You fully re-create an object from nothing, even if the object was destroyed. To do so, you must be able to picture the object in your mind. Additionally, the material component must be a remnant of the item, no matter how small or insignificant (even a speck of dust that remains from [[Disintegrate]] is enough). The spell fails if your imagination relied on too much guesswork; if the object would be too large to fit in a 5-foot cube; if the object still exists and you were simply not aware of it; or if the object is an artifact, has a level over 20, or has similar vast magical power.

The item reassembles in perfect condition. Even if your mental image was of a damaged or weathered object, the new one is in this perfected form. If the object was magical, this spell typically restores its constant magical properties, but not any temporary ones, such as charges or one-time uses. An item with charges or uses per day has all of its uses expended when remade, but it replenishes them normally thereafter.

**Source:** `= this.source` (`= this.source-type`)
