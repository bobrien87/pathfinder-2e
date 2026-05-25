---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Esoterica]]", "[[Fortune]]", "[[Manipulate]]", "[[Occult]]", "[[Thaumaturge]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You would attempt a roll affected by a misfortune effect.

You perform a superstition, such as casting salt over your shoulder to ward off bad luck. Turn Away Misfortune's fortune trait cancels out the misfortune effect, causing you to roll normally. As normal, you can apply only one fortune ability to a roll, so if you Turned Away Misfortune on an attack roll, you couldn't also use an ability like [[Halfling Luck]] to alter the roll further.

**Source:** `= this.source` (`= this.source-type`)
