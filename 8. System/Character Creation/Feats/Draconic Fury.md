---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Draconic Acolyte|Draconic Acolyte]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Concentrate]]"]
prerequisites: "Draconic Acolyte Dedication"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are holding or wearing your draconic gift.

You briefly summon spectral claws that lash out in a flurry. All creatures in a @Template[type:cone|distance:15] take @Damage[(1 + floor(@actor.level/4))d6[slashing]|options:area-damage] damage with a [[Reflex]] save against the higher of your class DC or spell DC. A creature that critically fails the save also takes @Damage[(floor(@actor.level/4))d4[persistent,bleed]] damage. If you are Channeling Draconic Essence, your spectral dragon's space can be the origin of the cone.

At 8th level and every 4 levels thereafter, the initial damage increases by 1d6 and the persistent bleed damage on a critical failure increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
