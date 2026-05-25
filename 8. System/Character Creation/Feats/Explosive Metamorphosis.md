---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Druid]]", "[[Spellshape]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You use additional primal energy to transform, creating a burst of elemental energy to complement your transformation. If your next action is to cast a non-cantrip morph or polymorph spell, select acid, cold, electricity, or fire. Your transformation creates a @Template[emanation|distance:5] around your new form that deals 1d6 damage of that type per rank of the spell. Each creature in that area attempts a basic Reflex save against your spell DC.

If your polymorph action had a trait corresponding to an energy type, you must select that one if possible. This action gains the trait corresponding to the energy type selected.

**Source:** `= this.source` (`= this.source-type`)
