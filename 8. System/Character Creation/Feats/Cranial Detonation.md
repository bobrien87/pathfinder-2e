---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Death]]", "[[Mindshift]]", "[[Psyche]]", "[[Psychic]]"]
frequency: "once per round"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per round

**Trigger** You successfully reduce one or more non-mindless enemies to 0 Hit Points with a spell.

As your overwhelming psyche fells a creature, you use its flickering consciousness to detonate psychic energy from the creature's head. Each enemy you reduced to 0 Hit Points dies and its head explodes. Each exploding head generates a shock wave in a @Template[emanation|distance:15] around that enemy. Each creature in any of the emanations takes @Damage[10d6[bludgeoning]|options:area-damage] damage with a [[Reflex]] save. If this damage reduces an enemy to 0 Hit Points, its head also explodes, potentially damaging more creatures and potentially causing more detonations. A given creature can take damage only once from a single use of Cranial Detonation.

**Source:** `= this.source` (`= this.source-type`)
