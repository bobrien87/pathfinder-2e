---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Mythic]]"]
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When the hero-gods built Pol-Sylirica and its seven armies, they feared betrayal from within. They took inspiration from the multi-headed hydra, and bound the seven armies together with supernatural ties to make them behave as if they shared one body. Following these tactics, during daily preparations, you can select a number of willing creatures equal to half your level to be part of your hydra's bond. Members of the same hydra's bond always know if another member is telling the truth.

When a member of the hydra's bond saves against an effect that would have them act against their allies (such as the [[Confused]] condition, a [[Dominate]] spell, or other mental effects that would give an ally the [[Controlled]] condition), you can spend a Mythic Point to allow that character to attempt the save at mythic proficiency. If a member of the hydra's bond fails a save against such an effect, other members automatically know that the target is controlled or under the influence of a mental effect. In addition, all members of the hydra's bond gain a +2 circumstance bonus to any roll made to counteract that effect.

**Source:** `= this.source` (`= this.source-type`)
