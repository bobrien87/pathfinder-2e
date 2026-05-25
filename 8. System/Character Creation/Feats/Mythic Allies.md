---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Mythic]]"]
prerequisites: "ability to cast spells from slots, at least one summon spell in your spellbook or repertoire"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You channel mythic power through your body and into a summoned ally, temporarily reinforcing them with a shared fraction of your mythic potential. Spend a Mythic Point; the summoned creature gains a +2 status bonus to its attack rolls, a +2 status bonus to all of its defenses, and a number of additional Hit Points equal to your level that last for the duration of its summoning. The next Strike made by the summoned creature after you use this ability gains a +4 circumstance bonus to the attack roll.

> [!danger] Effect: Mythic Allies

**Source:** `= this.source` (`= this.source-type`)
