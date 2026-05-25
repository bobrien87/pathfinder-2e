---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Exemplar]]", "[[Linguistic]]", "[[Mental]]"]
prerequisites: "You are not sanctified with the holy or unholy trait"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Having seen the wreckage left by the gods and their servitors as they play in their great war of good and evil, you've come to the only reasonable conclusion: they all must be cut from their silken thrones.

You swear a vow to defeat one creature within 60 feet that has the holy or unholy trait. The first time each round that you deal damage to that creature, you deal an additional 1d6 spirit damage.

You can't use Vow of Mortal Defiance again until you or the target is defeated, flees, or the encounter ends.

**Special** If you take this feat, you can't become sanctified with the holy or unholy trait. Retraining out of this feat typically requires a major change of philosophy.

**Source:** `= this.source` (`= this.source-type`)
