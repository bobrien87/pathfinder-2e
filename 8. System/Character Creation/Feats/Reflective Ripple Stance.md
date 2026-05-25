---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Monk]]", "[[Stance]]", "[[Water]]"]
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're unarmored.

You enter a stance of fluid grace as small amounts of water flow with your movements and attacks. You can make flowing wave attacks that deal 1d6 bludgeoning damage. They are in the brawling group and have the agile, disarm, finesse, nonlethal, trip, unarmed, and water traits. While in Reflective Ripple Stance, you gain a +1 circumstance bonus to Athletics checks to [[Disarm]], [[Swim]], or [[Trip]], and you gain a +2 circumstance bonus to your Reflex DC to avoid being Disarmed and Tripped.

**Special** This feat gains your choice of either the divine or occult trait, matching your qi spell tradition if possible.

**Source:** `= this.source` (`= this.source-type`)
