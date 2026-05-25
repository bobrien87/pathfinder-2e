---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Hungerseed]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Oni prefer large, cruel weapons for smashing their foes to pieces, and so do you. For the purposes of proficiency, you treat the [[Khakkhara]], [[Nodachi]], [[Ogre Hook]], and [[Tetsubo]] as simple weapons.

The ogre hook is an uncommon martial weapon that costs 1 gp, deals 1d10 piercing damage, has 2 Bulk, requires two hands to use, is in the pick weapon group, and has the deadly d10 and trip weapon traits.

At 5th level, whenever you get a critical hit with one of these weapons, or with your horns unarmed Strike, you get its critical specialization effect.

**Source:** `= this.source` (`= this.source-type`)
