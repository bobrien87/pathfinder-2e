---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Attack]]", "[[Centaur]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The greatest centaurs need not wait until their stories are over to touch the stars in the sky. You draw an arrow (or other ammunition), whisper a short invocation over it, and then Strike with a ranged weapon. The arrow becomes a bolt of starlight, changing its damage to your choice of force or spirit and granting it the effects of the *[[Ghost Touch]]* rune. When the arrow Strikes its target, it unravels into a constellation of starlight that wraps around the target's limbs, imposing a –10-foot circumstance penalty to its Speeds for 2d4 rounds or [[Immobilizing]] it if the Strike was critical hit. The target can untangle itself by spending an Interact action to break free.

**Source:** `= this.source` (`= this.source-type`)
