---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Auditory]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]", "[[Monk]]"]
prerequisites: "Dragon Stance"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are in [[Dragon Stance]]

You bellow, instilling fear in your enemies. Enemies within a @Template[emanation|distance:15] must succeed at a [[Will]] save against your Intimidation DC or be [[Frightened]] 1 ([[Frightened]] 2 on a critical failure). When a creature frightened by the roar begins its turn adjacent to you, it can't reduce its frightened value below 1 on that turn.

Your first attack that hits a frightened creature after you roar and before the end of your next turn gains a +4 circumstance bonus to damage.

After you use Dragon Roar, you can't use it again for 1d4 rounds. Its effects end immediately if you leave Dragon Stance. Creatures in the area are then temporarily immune for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
