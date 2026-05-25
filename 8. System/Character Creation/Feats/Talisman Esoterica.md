---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Esoterica]]", "[[Thaumaturge]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You know how to assemble the supernatural objects in your esoterica into a number of temporary talismans. Each day during your daily preparations, you can make two talismans with an item level no higher than half your level. You must know each talisman's formula. A talisman created this way is a temporary item and loses its magic the next time you make your daily preparations.

You know the formulas for all common talismans in GM Core of your level or lower. You remember your talisman formulas through oral tradition or mnemonics, so you don't need a formula book for them.

**Source:** `= this.source` (`= this.source-type`)
