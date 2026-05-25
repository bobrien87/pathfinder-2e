---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Champion]]"]
prerequisites: "lay on hands"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your touch soothes the body or mind. You can cast lay on hands targeting a living creature using 2 actions instead of 1. If you do, you can attempt to counteract one condition of your choice affecting the target. When you select this feat, choose one of the following options, which determines the conditions you can choose:

- **Mercy of the Body** [[Blinded]], [[Dazzled]], [[Deafened]], [[Enfeebled]], [[Sickened]];

- **Mercy of Grace** [[Clumsy]], [[Grabbed]], [[Paralyzed]];

- **Mercy of the Mind** [[Fleeing]], [[Frightened]], [[Stupefied]].

**Special** You can select this feat up to three times. Each time, choose a different type of mercy and add its options to those you can choose when you cast a 2-action lay on hands.

**Source:** `= this.source` (`= this.source-type`)
