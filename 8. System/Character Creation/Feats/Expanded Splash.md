---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Alchemist]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can throw bombs at just the right trajectory to create especially large and powerful explosions. When you throw an alchemical bomb and that bomb has the splash trait, you can have the splash damage affect all creatures within 10 feet of the target instead of 5 feet. If you do, you gain a status bonus to the bomb's splash damage equal to your Intelligence modifier. If you have the bomber 5th-level field discovery, this additional damage applies even if you caused your bomb to deal splash damage equal to your Intelligence modifier instead of the normal amount, allowing your bombs to deal splash damage equal to double your Intelligence modifier.

**Source:** `= this.source` (`= this.source-type`)
