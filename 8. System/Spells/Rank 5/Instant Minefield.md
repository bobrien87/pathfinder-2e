---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Fire]]", "[[Illusion]]", "[[Manipulate]]", "[[Subtle]]"]
cast: "`pf2:3`"
range: "100 feet"
defense: "basic Reflex"
duration: "10 minutes"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create several hidden mines throughout the area that explode when stepped on. Choose up to 6 unoccupied squares within range. A mine appears in each chosen square, visible only to you and your allies. A mine can't be targeted and isn't affected by area effects, but if it hasn't been triggered by the end of the spell's duration, it dissipates harmlessly. A creature that can see [[Invisible]] creatures and objects can see the mines. A creature can also attempt a Perception check against your spell DC to `act seek` to find an invisible mine.

A creature who enters a square with an invisible mine triggers it, causing an explosion that deals 3d6 fire damage and 3d6 piercing damage (basic Reflex save) to the creature and every creature in a @Template[emanation|distance:5] from the mine's square.

**Heightened (+1)** The fire damage and piercing damage dealt by a mine each increase by 1d6.

**Source:** `= this.source` (`= this.source-type`)
