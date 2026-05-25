---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Nagaji]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** Tian Xia origin or follower of Nalinivati

You channel the blessings of Nalinivati to transform into a manifestation of her will. You can cast 5th-rank [[Animal Form]] as an occult innate spell once per day, but you can choose only snake form with the spell. You can spend an additional action casting *animal form* to also cast 5th-rank [[Slither]] centered on your location; Nalinivati's will ensures that the shadow snakes created by the spell never harm you, so you're unaffected by the spell. If you Dismiss animal form, the effects of *slither* end as well.

**Source:** `= this.source` (`= this.source-type`)
