---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "expert in Religion, must worship a deity that lists "holy" or "unholy" in their sanctification"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You imbue water with your deity's blessing. Choose a container of water with light Bulk possessed by you or an ally within your reach. Until the end of your next turn, it becomes holy water or unholy water. You can choose holy water if your deity allows holy sanctification, unholy water if your deity allows unholy sanctification, or either if your deity allows both sanctifications. This is a temporary effect and doesn't impart monetary value or allow the water to be used for costs of rituals or the like. If you're a master in Religion, you can sanctify two containers when you take this action, and if you're legendary, you can sanctify three.

**Source:** `= this.source` (`= this.source-type`)
