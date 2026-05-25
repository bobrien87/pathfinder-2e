---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Surki]]"]
frequency: "once per PT1H"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Trigger** You attempt a saving throw against an area effect from the tradition matching your magiphage ability.

You consume the magic of an incoming spell or effect to protect your allies, though you might give yourself indigestion. Attempt a counteract check against the triggering effect; your counteract rank equals half your level (rounded up), and for the roll, use either your class DC – 10 or your spellcasting attribute modifier plus your spellcasting proficiency bonus. If you counteract the triggering effect, you end the effect for all other creatures in the area, but you become [[Sickened]] 1 as your body struggles to absorb the influx of magic.

**Source:** `= this.source` (`= this.source-type`)
