---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Jotunborn]]", "[[Manipulate]]", "[[Occult]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You stomp and unleash a wave of the magic of creation in a @Template[type:emanation|distance:30] that transforms non-magical difficult terrain and greater difficult terrain into normal terrain. This terrain transformation remains in place for 1 minute, after which the terrain returns to its original state.

Your stomp can also counteract magical difficult terrain and magical greater difficult terrain. Your stomp's counteract rank equals half your level (rounded up), and for the roll, use either your class DC – 10 or your spellcasting attribute modifier plus your spellcasting proficiency bonus. If you successfully counteract the triggering effect, you suppress the effect for 1 minute, after which the effect returns if its duration hasn't expired.

**Source:** `= this.source` (`= this.source-type`)
