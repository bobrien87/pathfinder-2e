---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Mythic]]"]
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

At one time, the hero-gods could not tell their own prophecies. Ongalte, hero-god of deicide, defied this rule and cemented why it should be upheld. Those that can reach into the web of fates and pluck out a string are forbidden from speaking of their own myth. Yet nothing forbids them from speaking the myths of others.

You peer through the world around you to see the delicate threads connecting others to their fate when they become afflicted. Choose a creature within 30 feet that you can see and who you know is affected by an ongoing affliction that progresses through stages, such as most diseases or poisons. Spend 1 Mythic Point, then attempt a [[Religion]] check at mythic proficiency against that affliction's DC.
- **Critical Success** The next time the afflicted creature attempts a saving throw against the affliction, they automatically gain a critical success. If this results in the affliction coming to an end, you gain 1 Mythic Point.
- **Success** The next time the afflicted creature attempts a saving throw against the affliction, they gain a +1 circumstance bonus to the roll and increase the result of the saving throw by one degree of success.
- **Failure** The next time the afflicted creature attempts a saving throw against the affliction, they gain a +1 circumstance bonus.
- **Critical Failure** You share the afflicted's fate, and are exposed to their affliction. You must immediately save against the affliction's effect.

**Source:** `= this.source` (`= this.source-type`)
