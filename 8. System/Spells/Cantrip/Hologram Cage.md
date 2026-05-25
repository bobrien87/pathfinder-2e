---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Illusion]]", "[[Light]]", "[[Manipulate]]", "[[Psychic]]"]
cast: "`pf2:3`"
range: "60 feet"
area: "20-foot cube"
duration: "1 minute"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** 1 cube 20 feet on each side

You weave light into a cube of vivid and fantastic patterns. The walls shed bright light for 10 feet (and dim light for the next 20 feet) and completely block line of sight; creatures within the cage can't be seen by creatures outside of it, though they can see each other, and creatures outside of it can't see into it. You can [[Dismiss]] the spell, and if you Cast the Spell again, your previous *hologram cage* ends.

**Heightened (7th)** The range of the spell increases to 80 feet, and you can expand the cube to be 25 feet on each side.

**Source:** `= this.source` (`= this.source-type`)
