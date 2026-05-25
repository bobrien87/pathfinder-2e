---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Illusion]]", "[[Manipulate]]", "[[Subtle]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 container of 2 Bulk or less"
duration: "1 hour"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You render every item inside the container you touch [[Invisible]], although the container itself remains visible. The items within are [[Undetected]] to all creatures, though a creature can attempt to find an item by reaching into the bag, making an item hidden to them instead if they succeed. Additionally, the spell doesn't prevent the items from making protrusions in the bag, adding weight, making noise when jostling around, and so on. However, the spell prevents anything within the container from falling out if it's upended. Any object removed from the container becomes visible and remains visible even if returned to the container.

**Heightened (4th)** The duration is until the next time you make your daily preparations.

**Source:** `= this.source` (`= this.source-type`)
