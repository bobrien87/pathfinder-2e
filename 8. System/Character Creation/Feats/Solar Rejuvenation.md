---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Ghoran]]", "[[Leshy]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Ghoran** - The warmth and light of the sun gives you life. If you rest outdoors for 10 minutes during the day, you regain Hit Points equal to your @Damage[(floor(@actor.level/2)*@actor.abilities.con.mod)[healing]]{Constitution modifier × half your level}. You gain this benefit in addition to any healing from [[Treat Wounds]].

**Leshy** - If you rest outdoors for 10 minutes during the day, you regain Hit Points equal to your @Damage[(floor(@actor.level/2)*@actor.abilities.con.mod)[healing]]{Constitution modifier × half your level}. You gain this benefit in addition to any healing from [[Treat Wounds]]. Leshies whose plant nourishment does not rely on photosynthesis require a similarly suitable environment. For example, fungus leshies need dark, damp environments and a pile of decaying plant matter.

**Source:** `= this.source` (`= this.source-type`)
