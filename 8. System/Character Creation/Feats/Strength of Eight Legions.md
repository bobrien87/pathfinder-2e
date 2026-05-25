---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Polymorph]]", "[[Primal]]", "[[Yaksha]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You meditate for 24 hours in a one-time ceremony within a forest or cave; after your seclusion, your frame and limbs swell with warlike might to enact your vows. You permanently gain the effects of [[Enlarge]], and your maximum Hit Points increase by your level. The ceremony transforms most of your gear to the appropriate size for your new body (though powerful items like artifacts or items strongly tied to their original size can't transform, at the GM's discretion).

**Source:** `= this.source` (`= this.source-type`)
