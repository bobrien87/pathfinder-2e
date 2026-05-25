---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Scrying]]", "[[Water]]"]
cast: "1 minute"
range: "touch"
targets: "1 gallon of water or more"
duration: "10 minutes (sustained)"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You touch the water's surface, and as the ripples spread out, so do your senses. When you Cast this Spell, you automatically know the location of any unoccupied, flowing water with a surface area of at least 1 square within 500 feet. You can pick any one of these streams to see and hear out of for the duration of the spell, though your field of vision is perpendicular to the flowing surface. For example, you could look normally out of a waterfall but would look straight up from out of a river. Each time you Sustain the spell, you can change to a different water source or move elsewhere along the same one.

If the water you're scrying through ceases flowing, such as by a faucet turning off, a river damming, or a waterfall freezing over, this spell ends. Additionally, your face appears as a faint reflection in the water's surface as you peek through. A creature that Seeks and succeeds at their Perception check against your spell DC detects your presence in the water.

**Heightened (5th)** You know the location of and can scry through flowing water within 1 mile.

**Source:** `= this.source` (`= this.source-type`)
