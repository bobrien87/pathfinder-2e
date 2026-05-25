---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Animist]]", "[[Apparition]]", "[[Divine]]", "[[Wandering]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your attuned apparition grants Mountain Lore as an apparition skill.

You surge forward inexorably. You Stride twice. At any point during this movement, you can [[Shove]] up to two creatures you pass adjacent to. When you end the movement, the turbulent spirits you're attuned to reward you for acting in an appropriately fierce manner: you and each ally in a @Template[type:emanation|distance:30] gain temporary Hit Points equal to half your level if you successfully Shoved at least one enemy, or equal to your level if you succeeded at Shoving both. These temporary Hit Points last until the beginning of your next turn.

> [!danger] Effect: Roaring Heart

**Source:** `= this.source` (`= this.source-type`)
