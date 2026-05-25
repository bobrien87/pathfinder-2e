---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Manipulate]]", "[[Teleportation]]"]
cast: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You step into a blazing fire that's big enough for you to fit inside and instantly teleport to any other fire within 5 miles that also has a sufficiently large size. Once you enter the first fire, you instantly know the rough locations of other sufficiently large fires within range and can exit from the original fire, if you prefer. You can't carry extradimensional spaces with you; if you attempt to do so, the spell fails.

**Heightened (6th)** The fire you exit can be up to 50 miles away.

**Heightened (8th)** The fire you exit can be up to 500 miles away.

**Heightened (9th)** The fire you exit can be anywhere on the same planet.

**Source:** `= this.source` (`= this.source-type`)
