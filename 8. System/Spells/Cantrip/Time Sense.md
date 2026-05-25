---
type: spell
sub-type: "Cantrip"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Concentrate]]"]
cast: "`pf2:1`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

When you Cast the Spell, you gain a perfect sense of time. You can learn exactly what time it is, down to the second. You can instead choose to gain a perfect sense of the calendar if you have knowledge in that area—if you're trained in Nature, you can learn exactly how long it is until sunrise and how many days until the next solstice. If you're trained in Astronomy Lore, you can learn precisely when any known predictable astronomical conjunction will begin and end, and so on.

You can gain a +1 status bonus to one attack roll, Perception check, saving throw, or skill check you take on the same turn you cast time sense that requires extremely precise timing. If you choose to gain this bonus, you can't gain it again for 1 hour.

**Source:** `= this.source` (`= this.source-type`)
