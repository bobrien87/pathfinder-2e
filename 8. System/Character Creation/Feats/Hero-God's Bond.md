---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Warrior Of Legend|Warrior Of Legend]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Warrior of Legend Dedication"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

At times, the myth of a hero-god includes a favored partner or a bonded ally, such as the hero-gods of promises and shield-bearers, Upion and Warrick. When you gain this feat, select an ally. They are your bonded partner. While you and your bonded partner are on the same plane, you and your bonded partner always have the same doomed value (defaulting to the highest value), so when your bonded partner's doomed condition would increase or be set to a specific amount, your doomed value also increases to match (if it is lower than your current doomed value). When either of you are [[Dying]], the other knows this immediately, as well as the distance and direction to the dying partner's location. When either of you attempts a recovery check, as long as the other is on the same plane, you gain a +2 circumstance bonus to the check. You can communicate telepathically with your bonded partner as long as you are within 60 feet of each other.

You can change your bonded partner by spending 1 week of downtime bonding with another ally.

**Source:** `= this.source` (`= this.source-type`)
