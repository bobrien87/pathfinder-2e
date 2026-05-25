---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Animist]]", "[[Apparition]]", "[[Aura]]"]
prerequisites: "Channeler's Stance"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are in Channeler's Stance and your last action was to Cast a Spell from your spell slots.

Your apparition uses excess energy to protect you. You and all adjacent allies gain a +1 status bonus to your AC and to your Reflex saving throws until the start of your next turn. If the spell was at least 7th rank, the status bonus increase to +2.

> [!danger] Effect: Channeled Protection

**Source:** `= this.source` (`= this.source-type`)
