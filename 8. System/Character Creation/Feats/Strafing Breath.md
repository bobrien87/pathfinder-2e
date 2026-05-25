---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Drake Rider|Drake Rider]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "War Rider Stance"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** [[War Rider Stance]] is active.

You urge your dragon mount forward, wreathed in magical power. Your mount Strides three times. If your mount has a fly Speed, it can substitute a Fly action for any of these Stride actions. As it moves, your dragon companion's magical breath billows around you. The aura from War Rider Stance increases to a @Template[type:emanation|distance:10] during this movement, and each creature that's in the emanation at any point during your movement takes the damage from it (with the normal save). A creature can take damage only once, even if you move past it multiple times.

**Source:** `= this.source` (`= this.source-type`)
