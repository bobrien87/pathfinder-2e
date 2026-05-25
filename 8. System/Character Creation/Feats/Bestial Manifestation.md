---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Nephilim]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Part of your body has an animalistic influence from a planar creature. Your hands end in claws, you have hooves instead of feet, sharp teeth fill your mouth, or a tail extends from your spine. You gain your choice of one of the following unarmed attacks. The attack is in the brawling group and has the listed damage die and traits.

**Claw** 1d4 slashing (agile, finesse, unarmed, versatile piercing)

**Hoof** 1d6 bludgeoning (finesse, unarmed)

**Jaws** 1d6 piercing (finesse, unarmed)

**Tail** 1d4 bludgeoning (agile, finesse, unarmed)

**Special** You can select this feat only at 1st level, and you can't retrain into or out of this feat, nor can you change the type of attack you gained.

**Source:** `= this.source` (`= this.source-type`)
