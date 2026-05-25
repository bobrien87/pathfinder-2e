---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Draconic Acolyte|Draconic Acolyte]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Aura]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]"]
prerequisites: "Draconic Acolyte Dedication"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are holding or wearing your *draconic gift*.

Draconic essence coruscates around you, sapping the resilience of your foes. Each enemy in a @Template[type:emanation|distance:20] must attempt a Will saving throw against the higher of your class DC or spell DC. If you are Channeling Draconic Essence, your spectral dragon can be the origin of this emanation. Regardless of the result of its saving throw, a creature that attempts a save is temporarily immune to your Frightening Power for 24 hours.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Frightened]] 1.
- **Failure** The creature is [[Frightened]] 2.
- **Critical Failure** The creature is [[Frightened]] 4.

**Source:** `= this.source` (`= this.source-type`)
