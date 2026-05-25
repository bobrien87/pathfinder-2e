---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Yaoguai]]"]
prerequisites: "born of item, born of elements, or born of vegetation heritage"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You take on the shape you had before you awoke to hide in plain sight. When you Change Shape, you can assume the form of an immobile plant, object, or natural feature of Tiny, Small, or Medium size, as suits your heritage. Using your immobile form counts as setting up a disguise for the Impersonate use of Deception, except that you can Impersonate an object instead of a creature, it gives you a +4 status bonus to Deception checks to prevent others from seeing through your disguise, and you add your level even if you're untrained. You can speak while in immobile form, but you can't attack, cast spells, or move.

**Source:** `= this.source` (`= this.source-type`)
