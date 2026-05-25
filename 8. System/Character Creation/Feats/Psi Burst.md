---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Mindshift]]", "[[Occult]]", "[[Psyche]]", "[[Psychic]]"]
frequency: "once per round"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per round

With a passing thought, you direct violent psychic energies at a nearby creature. Target one creature within 30 feet. It takes @Damage[(ceil(@actor.level/2)d4)[bludgeoning]] damage with a [[Reflex]] save. At 3rd level and every 2 levels thereafter, the damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
