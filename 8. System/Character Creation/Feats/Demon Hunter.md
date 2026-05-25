---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Elf]]"]
prerequisites: "expert in Religion or Demon Lore"
source: "Pathfinder #210: Whispers in the Dirt"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The demons of Tanglebriar have long haunted your dreams, just as they have long threatened Kyonin. You have not only studied these fiendish foes well, but have trained extensively to battle the hordes of demons that serve Treerazer and are particularly adept at striking desperate melee blows against them.

When you make your daily preparations, choose one kind of demon, such as succubus, omox, shemhazian, or Treerazer. For the remainder of the day, the first time you hit one of those specific demons in a round with a melee Strike, you also deal 1d6 additional spirit damage. At 13th level, the extra damage increases to 2d6 additional spirit damage, and at 17th level, the extra damage increases to 3d6 spirit damage.

**Source:** `= this.source` (`= this.source-type`)
