---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Drake Rider|Drake Rider]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Flair Rider Stance, Wing Rider"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are riding your dragon companion and are airborne.

You guide your mount into a plummet, diving headlong at a single foe. You command your mount to Fly twice. It must end this movement at a lower altitude than it began its turn at. You and your mount gain a +4 circumstance bonus to AC against reactions triggered by this movement. At the end of this movement, your mount attempts a melee Strike against one creature in its reach. If the Strike hits, the target is knocked [[Prone]] if it's smaller than your mount; if it's a critical hit, the target is knocked prone if it's the same size as your mount or smaller.

**Source:** `= this.source` (`= this.source-type`)
