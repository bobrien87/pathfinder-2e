---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wildspell|Wildspell]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]", "[[Stance]]"]
prerequisites: "Wildspell Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You cast [[Spellsurge]].

Your aura links your friends together with mystic strands. While you're in this stance, an ally within your *spellsurge* aura can treat any other ally within the aura as the point of origin for a spell they cast, calculating range and cover from the other creature's space instead of their own. This allows all allied creatures within your *spellsurge* aura to act as though they're in touch range of each other since each creature is in touch range of itself. Additionally, while you're in this stance, an ally casting a spell that targets only the caster can have that spell affect any other ally within your *spellsurge* aura instead.

**Source:** `= this.source` (`= this.source-type`)
