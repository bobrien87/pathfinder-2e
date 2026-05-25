---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Surki]]"]
prerequisites: "Vestigial Magicsense"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature you could reach with a Stride action Casts a Spell from the tradition matching your magiphage ability.

You move reflexively toward the source of magic you most consumed as a larva. You Stride, and you must end your movement adjacent to the triggering creature. You then can't use Magitaxis against the triggering creature for 24 hours as your reflexes reacclimate, though you can use it against other creatures.

You can use Magitaxis while Burrowing, Climbing, Flying, or Swimming instead of Striding (changing the trigger accordingly) if you have the corresponding movement type.

**Source:** `= this.source` (`= this.source-type`)
