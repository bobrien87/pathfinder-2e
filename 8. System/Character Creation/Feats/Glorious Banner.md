---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Commander]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your banner is an awesome sight to behold. Your commander's banner now affects a @Template[type:emanation|distance:60] (or an @Template[type:burst|distance:80] if you are using Plant Banner); the status bonus to Will saves and DCs against fear effects granted to your allies increases to +2; and you and affected allies gain a +1 status bonus to AC, Fortitude saves, and Reflex saves. Enemies within the aura of your commander's banner take a –2 status penalty to Will saves as long as they can see your banner.

**Source:** `= this.source` (`= this.source-type`)
