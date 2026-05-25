---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "expert in Medicine, expert in Performance"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With your experience as a performer, you can keep a set of medical tools handy at all times. You can wear a healer's toolkit as part of any costume or disguise. Creatures will generally only notice the toolkit it if they use a [[Seek]] action and succeed at a [[Perception]] check against your Performance DC. In addition, you can realize at the last moment when you should just be pretending to avoid doing any lasting harm.

When you critically fail a Medicine check to Administer First Aid, [[Treat Disease]], [[Treat Poison]], or [[Treat Wounds]], you can attempt a Performance check against the patient's Perception DC. On a success, your critical failure at the Medicine check becomes a failure.

**Source:** `= this.source` (`= this.source-type`)
