---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Necrologist|Necrologist]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Concentrate]]", "[[Emotion]]", "[[Fear]]", "[[Flourish]]", "[[Magical]]", "[[Mental]]"]
prerequisites: "Ghostsong"
frequency: "once per PT10M"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

**Requirements** Your horde is raised and consists of spirits.

The voices of the spirits you command spark fear in the hearts of your enemies. You Sustain your horde and command those spirits to shriek in unison. Each living enemy within a @Template[type:emanation|distance:20] from your horde takes @Damage[ternary(lte(@actor.level, 12),5,(floor(@actor.level/2)-1))d10[mental]|options:area-damage] damage, depending on its [[Will]] save saving throw against your spell DC. This damage increases by 1d10 at 14th level and every 2 levels thereafter.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and is [[Frightened]] 1.
- **Failure** The creature takes full damage and is [[Frightened]] 2.
- **Critical Failure** The creature takes double damage and is [[Frightened]] 3.

**Source:** `= this.source` (`= this.source-type`)
