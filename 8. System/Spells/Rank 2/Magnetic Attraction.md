---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Metal]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "up to 10 metal objects with a total Bulk of 1 or less"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You adjust your magnetic polarity, plucking daggers from hands and coins from belts. The targeted objects fly to your location, letting you catch them easily in your hands, or dropping to the ground at your position, at your discretion. Unattended objects fly to you automatically. If you target secured objects or those in another creature's possession (such as sheathed weapons), you must attempt to Disarm the creature of the metal objects, making a spell attack roll instead of an Athletics check to do so.

Instead of drawing the objects to yourself, you can polarize a single metal object within range, designating it as a lodestone and causing the metal objects to fly to it instead. The lodestone must be at least three times the total Bulk of the targeted metal objects. Objects will stick to the lodestone for 1 minute, though they can be wrenched away with an Interact action.

**Source:** `= this.source` (`= this.source-type`)
