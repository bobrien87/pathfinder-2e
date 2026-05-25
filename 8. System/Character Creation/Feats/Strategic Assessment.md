---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Investigator]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You learn your foes' strengths and weaknesses by watching them move. When you hit a creature with a Strike on which you substituted your attack roll due to Devising a Stratagem, the GM chooses one of the following pieces of information about the enemy to tell you.

- Which of the enemy's weaknesses is highest
- Which of the enemy's resistances is highest
- Which of the enemy's saving throws is lowest
- One immunity the enemy has

The GM can choose deliberately or at random, but they can't choose information that doesn't apply (such as choosing an immunity for an enemy that has no immunities). This applies only the first time you hit a given creature.

**Source:** `= this.source` (`= this.source-type`)
