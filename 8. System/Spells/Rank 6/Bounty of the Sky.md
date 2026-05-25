---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Healing]]", "[[Manipulate]]", "[[Mythic]]"]
cast: "`pf2:2`"
area: "30-foot emanation"
duration: "1 minute"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call forth a flock of geese that drop restorative fruits and breads from the sky as they fly overhead. You or an ally in the area can Interact to collect one of these gifts, and can then either consume it as part of the same action or do so with a separate Interact action later in the spell's duration. Enemies who attempt to pick up one of these gifts find that it turns to ash in their hands. Each time a character consumes one of these gifts, they can select one of the following benefits.

- The character regains 4d6 Hit Points.
- The character reduces the stage of one poison or disease they suffer from by one stage. This can't reduce the stage below 1 or cure the affliction.
- The character reduces the value of their [[Clumsy]], [[Drained]], [[Enfeebled]], or [[Stupefied]] condition by 2, or reduces two of the listed conditions by 1 each.

**Heightened (+2)** The amount of Hit Points a character regains from consuming a gift increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
