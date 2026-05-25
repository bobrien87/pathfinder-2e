---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Amp]]", "[[Mental]]", "[[Occult]]", "[[Psychic]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your spell leaves a lingering connection between you and a creature-one through which you can nudge the creature's mind this way or that. The amped cantrip must take 2 or more actions to cast, target one or more creatures, and either require a spell attack roll or have a saving throw. Use this amp in place of the psi cantrip's normal amp entry.

**Amp** Choose one enemy who is a target of the spell. If that enemy fails its save or the spell hits it, you whisper in the creature's mind, forcing it to [[Stride]] up to half its Speed in a direction of your choosing; as this is forced movement, you can't force the creature to move into hazardous terrain, off a ledge, or the like. After it moves, the creature becomes temporarily immune to this amp for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
