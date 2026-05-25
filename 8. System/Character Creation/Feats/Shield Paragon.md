---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Champion]]"]
prerequisites: "blessed shield"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your shield is a vessel of divine protection. When you're wielding your chosen shield, it is always raised, even without you using the Raise a Shield action.

If the shield would be destroyed, it vanishes to your deity's realm instead, where a servitor of your deity repairs it. During your next daily preparations, the shield returns to you fully repaired. While the shield is gone, you can spend 1 minute to infuse a different shield with your blessed shield benefit until your true shield returns

**Source:** `= this.source` (`= this.source-type`)
