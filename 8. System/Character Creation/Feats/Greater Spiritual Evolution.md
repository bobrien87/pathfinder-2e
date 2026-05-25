---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Sorcerer]]"]
prerequisites: "Divine Evolution or Occult Evolution"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your magical blood allows your spells to be fully effective against incorporeal creatures. Your spells have the effects of a [[Ghost Touch]] property rune. They can target or affect a creature projecting its consciousness (such as via [[Project Image]]) or possessing another creature, even if its body is elsewhere, though you must know about the possession or projection and choose to do so. Your spells can affect creatures on the Ethereal Plane, though this doesn't grant you the ability to locate them.

**Source:** `= this.source` (`= this.source-type`)
