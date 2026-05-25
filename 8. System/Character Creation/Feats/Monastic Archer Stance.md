---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Monk]]", "[[Stance]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are unarmored and wielding a longbow, shortbow, or a bow with the monk trait.

You enter a specialized stance for a unique martial art centered around the use of a bow. While in this stance, the only Strikes you can make are those using longbows, shortbows, or bows with the monk trait.

You can use [[Flurry of Blows]] with these bows. You can use your other monk feats or monk abilities that normally require unarmed attacks with these bows when attacking within half the first range increment (normally 50 feet for a longbow and 30 feet for a shortbow), so long as the feat or ability doesn't require a single, specific Strike.

> [!danger] Effect: Stance: Monastic Archer Stance

**Special** When you select this feat, you become trained in the longbow, shortbow, and any simple and martial bows with the monk trait. If you gain the expert strikes class feature, your proficiency rank for these weapons increases to expert, and if you gain the master strikes class feature, your proficiency rank for these weapons increases to master.

**Source:** `= this.source` (`= this.source-type`)
