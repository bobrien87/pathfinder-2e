---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Lizardfolk]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your weapons are those you were born with. Choose one of the following options:

- **Claws** Your claw attack deals 1d6 slashing damage instead of 1d4 and gains the versatile P trait.
- **Fangs** You gain a fangs unarmed attack that deals 1d8 piercing damage and is in the brawling group.
- **Tail** You gain a tail unarmed attack that deals 1d6 bludgeoning damage, is in the brawling group, and has the sweep trait.

At 5th level, whenever you get a critical hit with one of the unarmed attacks you have gained or improved with this feat, you get its critical specialization effect.

**Special** You can take this feat multiple times, choosing a different unarmed attack option each time.

**Source:** `= this.source` (`= this.source-type`)
