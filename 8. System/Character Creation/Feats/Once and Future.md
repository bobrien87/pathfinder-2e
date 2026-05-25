---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Prophesied Monarch|Prophesied Monarch]]"
source-type: "Remaster"
level: "20"
traits: ["[[Mythic]]"]
prerequisites: "Prophesied Monarch Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Though foul treachery might lay you low or dark magic still your heart, when the people cry out for you in desperate need, you shall rise to protect them. You can't die except due to old age as long as one of your knights is alive and within 30 feet; if your dying or doomed condition would increase to a high enough value to kill you, it doesn't increase, and any effect that would instantly kill you instead just reduces you to 0 Hit Points. The first time each year you would die for any reason other than old age, you instead return to life and consciousness with a number of Hit Points equal to twice your level and gain a Mythic Point. If you ever truly die and aren't returned to life within 1 year, you're reborn as a child into a new mortal body somewhere in the world where stories of your accomplishments are still told. You don't complete your journey along the River of Souls until all mortal memory of you has vanished.

**Source:** `= this.source` (`= this.source-type`)
