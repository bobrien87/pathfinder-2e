---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Amp]]", "[[Illusion]]", "[[Mental]]", "[[Occult]]", "[[Psychic]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your spell reaches into the mind of a creature and removes you from it. The amped cantrip must be one that has one or more targets and must either require a spell attack roll or have a saving throw. Use this amp in place of the psi cantrip's normal amp entry.

**Amp** Choose one target of the spell or one creature in its area. If that enemy fails its save or the spell hits it, you become undetected by that creature, disappearing from its senses for 1 minute or until you use a hostile action. This is similar to being [[Invisible]], but effects like *see the unseen *don't reveal you-you're affecting the target's mind, not its vision. *Truesight* can still see through this illusion if the counteract check succeeds.

**Source:** `= this.source` (`= this.source-type`)
