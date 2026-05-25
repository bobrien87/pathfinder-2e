---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Tanuki]]"]
prerequisites: "Teakettle Form"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

An inconspicuous statue in front of a shop is the perfect form to wait for things to blow over. When you Change Shape, you can assume the form of a statue, shop sign, or other heavy object of up to Large size. Using statue form counts as setting up a disguise for the Impersonate use of Deception, except that you can Impersonate an object instead of a creature, it gives you a +4 status bonus to Deception checks to prevent others from seeing through your disguise, and you add your level even if you're untrained. Your weight increases to match the object you're impersonating while in statue form, allowing you to use your spell DC or your class DC instead of the relevant DC to resist forced movement (usually Fortitude), if they're higher. You can speak while in statue form, but you can't attack, cast spells, or move.

**Source:** `= this.source` (`= this.source-type`)
