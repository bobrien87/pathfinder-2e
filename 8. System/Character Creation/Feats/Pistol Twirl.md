---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Gunslinger]]"]
prerequisites: "trained in Deception"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a loaded one-handed ranged weapon.

Your quick gestures and flair for performance distract your opponent, leaving it vulnerable to your follow-up attacks. You [[Feint]] against an opponent within the required weapon's first range increment, rather than an opponent within melee reach. If you succeed, the foe is [[Off Guard]] against your melee and ranged attacks, rather than only your melee attacks. On a critical failure, you're off-guard against the target's melee and ranged attacks, rather than only its melee attacks.

**Source:** `= this.source` (`= this.source-type`)
