---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pistol Phenom|Pistol Phenom]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in at least one type of one-handed firearm, trained in Deception, trained in Performance"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You catch an opponent [[Off Guard]] by spinning your weapon. You gain the Pistol Twirl gunslinger feat, enabling you to [[Feint]] against creatures within your weapon's first range increment. This otherwise serves as [[Pistol Twirl]] for the purpose of meeting prerequisites, although as normal, it doesn't count as another pistol phenom feat for the purpose of meeting Pistol Phenom Dedication's special entry and taking another archetype. Whenever you Feint with a one-handed firearm, you can choose to attempt a Performance check instead of a Deception check.

Pistol Phenom

**Source:** `= this.source` (`= this.source-type`)
