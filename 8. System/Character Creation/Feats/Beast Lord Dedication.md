---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beast Lord|Beast Lord]]"
source-type: "Remaster"
level: "12"
traits: ["[[Destiny]]", "[[Mythic]]"]
prerequisites: "a mature animal companion or an advanced construct companion"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your Calling has united your destiny with a companion, harnessing a connection between you that links your minds, hearts, and souls. Choose a companion that qualified you for this feat as your united companion. Your united companion increases its Intelligence modifier to +0 or by 1 if its Intelligence modifier is greater than +0. It gains the ability to understand a language that you know and can communicate with you, but only you can understand your companion when it speaks, as it uses chirps, grunts, or other noises to convey its meaning. If you or your united companion are conscious and within 30 feet of each other and either must attempt a saving throw against a mental effect, both you and your united companion attempt the saving throw. The target of the effect uses the best result; this also applies if both you and your united companion must attempt a saving throw against the same effect.

Beast Lord

**Source:** `= this.source` (`= this.source-type`)
