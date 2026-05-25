---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Sorcerer]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can wrap your magic around you like a cloak that causes those who dare to target you with spells to suffer a similar fate. You know the following blood magic effect.

**Blood Magic—Reflect Harm** Your blood ensures that those who harm you with magic are harmed in return. The first time you take damage from a spell before the beginning of your next turn, attempt spell attack roll against the creature who cast the triggering spell. On a hit, the creature takes the same amount and type of damage that you just took. If you critically hit, the creature takes twice the damage.

**Source:** `= this.source` (`= this.source-type`)
