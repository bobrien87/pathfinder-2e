---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Infusion]]", "[[Kineticist]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With a signature flair, you shape blasts of elemental power into the form of a weapon, such as a sword made of whirling wind or a bow that shoots flames. If your next action is an Elemental Blast, choose a weapon shape for it to take. You can choose to change the blast's damage type to bludgeoning, piercing, or slashing-whichever suits the weapon shape-and you can choose other alterations depending on whether you make a melee or ranged blast.

- **Melee** Add one of the following traits of your choice: agile, backswing, forceful, reach, sweep.

- **Ranged** Choose one of three options: range increment 100 feet and the volley 30 feet trait, range increment 50 feet and the propulsive trait, or range increment 20 feet and the thrown trait.

**Source:** `= this.source` (`= this.source-type`)
