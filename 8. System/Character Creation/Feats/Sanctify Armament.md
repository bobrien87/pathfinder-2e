---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Cleric]]", "[[Divine]]"]
prerequisites: "holy or unholy trait"
frequency: "once per round"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You touch a weapon and bring it into concordance with your deity. For 1 round, that weapon gains your holy or unholy trait. It also deals an additional 2d6 spirit damage to creatures of the opposed trait. For example, if you are holy, the weapon would deal an extra 2d6 spirit damage to unholy creatures.

If you use Sanctify Armament again, any previous use of it expires.

> [!danger] Effect: Sanctify Armament

**Source:** `= this.source` (`= this.source-type`)
