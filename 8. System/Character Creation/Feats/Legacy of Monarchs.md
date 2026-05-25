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

No matter what might happen to you, your legacy shall never die. If you're slain, any of your knights who touches your corpse can choose to take up your mantle; over the course of 10 minutes, they don your equipment, replace their attribute modifiers with yours, replace their skills and feats with yours, and become you for all intents and purposes, retaining only their ancestry, heritage, and ancestry feats. If you're later returned to life, you can choose to reclaim your mantle from your former knight; if you do so, they revert to their previous state, and you reclaim all that was yours. Otherwise, you can choose to live a new life, retraining all your skills and feats while adopting a new name and identity.

**Source:** `= this.source` (`= this.source-type`)
