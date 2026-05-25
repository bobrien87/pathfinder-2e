---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Goblin]]"]
prerequisites: "dokkaebi goblin heritage"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can create illusory wisps of ghostly blue flame. You can cast [[Ignition]] as an innate occult cantrip at will. A cantrip is heightened to a spell rank equal to half your level rounded up. Your Dokkaebi Fire is purely illusory; while it emits light, it deals mental damage instead of fire damage (so it can't light objects on fire or affect mindless creatures), and it has the illusion and mental traits instead of the fire trait.

**Special** If you have the [[Burn It!]] feat, its effects apply to your dokkaebi fire even though it deals mental damage—dokkaebi consider these flames as real as any mortal fire, and so they are.

**Source:** `= this.source` (`= this.source-type`)
