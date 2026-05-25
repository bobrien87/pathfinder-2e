---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Lineage]]", "[[Talos]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your elemental lineage manifests in the polished gleam of precious metals, such as silver and gold, or even rare and valuable skymetals like adamantine or orichalcum. This natural luster enhances your charm; you become trained in your choice of Diplomacy or Society. If you would automatically become trained in both these skills (from your background or class, for example), you instead become trained in a skill of your choice. If you're trained in Society, you also gain the [[Courtly Graces]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
