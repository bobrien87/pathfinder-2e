---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[General]]", "[[Healing]]", "[[Manipulate]]", "[[Skill]]"]
prerequisites: "trained in Occultism"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You know how to stimulate a body's natural healing abilities through the application of resonant crystals. Doing so requires you to use at least two semiprecious stones with a total value of 5 gp or more in place of a healer's toolkit, which allows you to attempt to `act treat-disease` or `act treat-poison` using Occultism rather than Medicine.

If you're an expert in Occultism and you use gems whose total value equals or exceeds 50 gp, you gain a +1 item bonus to your Occultism check. If you're a master and the gems' value equals or exceeds 700 gp, the item bonus increases to +2; if you're legendary in Occultism and the gems' value equals or exceeds 15,000 gp, the item bonus increases to +3.

**Source:** `= this.source` (`= this.source-type`)
