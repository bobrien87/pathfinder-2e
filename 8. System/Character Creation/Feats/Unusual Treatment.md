---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "expert in Medicine"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your medical training extends to less obvious conditions. When you succeed against a DC 20 check to [[Treat Wounds]], you can also reduce the value of one [[Clumsy]], [[Enfeebled]], or [[Stupefied]] condition on the patient by 1. If you're able to treat more than one creature at once, choose only one to gain this benefit. A creature can benefit from Unusual Treatment only once per day. If the condition results from an affliction, the affliction isn't cured, though the condition is reduced as long as the affliction remains at that stage. If you are a master in Medicine, add the [[Drained]] condition to the list of conditions you can remove if you succeed at a DC 30 check. If you are legendary in Medicine, you reduce the chosen condition by 2 instead of by 1.

**Source:** `= this.source` (`= this.source-type`)
