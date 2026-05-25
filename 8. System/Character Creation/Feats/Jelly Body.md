---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Aftermath]]", "[[Magical]]"]
prerequisites: "You've been reduced to 0 Hit Points while engulfed by an ooze."
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Some of the ooze that surrounded you made its way permanently into parts of your body, turning you soft to the touch and semitransparent enough to show bones. You gain resistance equal to your level to precision damage and damage from critical hits. You can submerge up to 1 Bulk of items within your body by sticking them inside of yourself. While the protrusion of the item is still visible from the outside, the items don't count toward making you encumbered or your maximum Bulk while stored in you. You can [[Interact]] to retrieve or store an item submerged into your body.

**Source:** `= this.source` (`= this.source-type`)
