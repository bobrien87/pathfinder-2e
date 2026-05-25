---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Draconic Acolyte|Draconic Acolyte]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Concentrate]]"]
prerequisites: "Draconic Acolyte Dedication"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are Channeling Draconic Essence.

Uncontainable power explodes from your spectral dragon. Your Channel Draconic Essence ends, and all creatures (except you) in a @Template[type:emanation|distance:10] from your spectral dragon take @Damage[(5+floor((@actor.level - 4)/2))d6|options:area-damage] damage with a [[Reflex]] save against the higher of your class DC or spell DC. The damage's type matches the breath of your draconic benefactor. You then can't use Essence Overflow again for 1d4 rounds.

At 8th level and every 2 levels thereafter, the damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
