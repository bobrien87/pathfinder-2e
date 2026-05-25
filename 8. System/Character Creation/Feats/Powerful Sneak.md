---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Rogue]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've learned to exploit your enemies' openings. Your sneak attack damage ignores any immunity or resistance the target has to precision damage. In addition, when you [[Sneak]], you can designate one creature you're undetected by at the end of that action. On the next attack you make against that creature before the end of your next turn, any sneak attack die you roll that's less than 3 is a 3 instead. This has no benefit if your next attack against the creature doesn't deal sneak attack damage, and if you designate a new creature you lose the benefit on any previous one.

**Source:** `= this.source` (`= this.source-type`)
