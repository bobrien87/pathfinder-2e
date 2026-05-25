---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Animist]]", "[[Misfortune]]", "[[Wandering]]"]
prerequisites: "Spirit Familiar"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You are targeted by an attack.

**Requirements** Your familiar is adjacent to you or in your space.

With a mere thought, you discorporate your familiar into a thousand shards of spiritual magic, protecting both it and yourself from physical harm while making it difficult for enemies to move near you. You are [[Concealed]] from the triggering attack. Until the start of your next turn, your familiar can't be targeted and your enemies treat all spaces adjacent to you as difficult terrain.

**Source:** `= this.source` (`= this.source-type`)
