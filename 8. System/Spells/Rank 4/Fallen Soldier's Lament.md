---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]", "[[Mental]]", "[[Visual]]"]
cast: "`pf2:2`"
range: "100 feet"
targets: "1 corpse of a Medium or smaller creature that has died within the past 8 hours"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You raise an illusion in the space of a fallen foe, crafting it to resemble a ghost of your target before parading it across the battlefield. Whenever you Cast this Spell or Sustain this spell, you move the illusion up to 30 feet and cause each enemy in a 30-foot emanation of the spirit to attempt a Will save against your spell DC. Enemies who fail become [[Frightened]] 1 (or [[Frightened]] 2 on a critical failure).

**Heightened (6th)** You can target a corpse of any size that has died within the past 8 hours.

**Source:** `= this.source` (`= this.source-type`)
