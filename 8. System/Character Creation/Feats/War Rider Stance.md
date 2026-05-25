---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Drake Rider|Drake Rider]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Aura]]", "[[Stance]]"]
prerequisites: "Drake Rider Dedication, expert in martial weapons, dragon companion with a support benefit that includes damage"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your dragon's constant breath threatens your foes. While in this stance, your dragon companion has an aura in a @Template[type:emanation|distance:5]. Each creature that starts its turn in the aura takes the damage listed under the dragon's support benefit with a basic Reflex save against your mount's Athletics DC.

**Source:** `= this.source` (`= this.source-type`)
