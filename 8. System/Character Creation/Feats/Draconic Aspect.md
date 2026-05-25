---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Dragonblood]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have an obvious draconic feature, such as sharp claws, a snout full of sharp teeth, or strong reptilian tail, that you can use offensively. You gain your choice of one of the following unarmed attacks. The attack is in the brawling group and has the listed damage die and traits.

- **Claw** 1d4 slashing (agile, finesse, unarmed)
- **Jaws** 1d6 piercing (forceful, unarmed)
- **Tail** 1d6 bludgeoning (sweep, trip, unarmed)

**Special** You can select this feat only at 1st level, and you can't retrain into or out of this feat, nor can you change the type of attack you gained.

**Source:** `= this.source` (`= this.source-type`)
