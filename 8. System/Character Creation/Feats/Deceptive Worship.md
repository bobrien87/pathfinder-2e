---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "trained in Occultism"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Members of your cult frequently pass themselves off as worshippers of other religions. You can use Occultism instead of Deception to [[Impersonate]] a typical worshipper of another faith or to [[Lie]] specifically to claim you are a member of the faith you are Impersonating. You still need to use the Deception skill to Impersonate a specific worshipper or to perform other deceptive actions, such as attempting to Lie about any other matter.

**Source:** `= this.source` (`= this.source-type`)
