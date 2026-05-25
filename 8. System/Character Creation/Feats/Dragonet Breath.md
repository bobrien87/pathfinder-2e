---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Dragonet]]"]
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have developed your magical breath. You expel the dragonet breath associated with your heritage. Dragonet Breath gains the traits listed in parentheses, and the DC is your class DC or spell DC, whichever is higher. After you use Dragonet Breath, you can't use it again for 1d4 rounds.

- **Fey Dragonet** (arcane, poison) You breathe a @Template[type:cone|distance:15] of euphoric gas. Each creature in the area must succeed at a [[Fortitude]] save or become [[Stupefied 1]] for 1 round.
- **Homing Drake** (acid) You expel a @Template[type:line|distance:30] of caustic spittle that deals @Damage[(ceil(@actor.level/2))d4[acid]|options:area-damage] damage with a [[Reflex]] save. At 3rd level and every 2 levels thereafter, the damage increases by 1d4.
- **House Drake** (arcane, mental) You breathe out a cloud of silver mist in a @Template[type:cone|distance:15] that deals @Damage[(ceil(@actor.level/2))d4[mental]|options:area-damage] damage with a [[Will]] save. It counts as silver for the purpose of weaknesses. At 3rd level and every 2 levels thereafter, the damage increases by 1d4.

- **Pearl Dragonet** (arcane, curse) You breathe a @Template[type:cone|distance:15] of golden mist that alters the luck of creatures caught in it. Each time you use Dragonet Breath, decide if it gives good luck or bad luck. Any creature affected by your Dragonet Breath becomes temporarily immune to it for 1 hour. If your breath gives good luck, each creature in the area gains a +1 status bonus to its next attack roll or skill check before the start of your next turn. If your breath gives bad luck, each creature in the area must attempt a [[Will]] save. A creature that fails its save takes a –1 status penalty to its next attack roll or skill check before the start of your next turn. On a critical failure, the creature must instead roll twice and take the worse result on the check; this is a misfortune effect.

- **Tidepool Dragonet** (fire) You breathe a @Template[type:line|distance:15] of superheated gas that deals @Damage[(ceil(@actor.level/2))d4[fire]|options:area-damage] damage with a [[Reflex]] save. At 3rd level and every 2 levels thereafter, the damage increases by 1d4. You can use your breath underwater even though it has the fire trait. If you do, it gains the water trait and emerges as a @Template[type:cone|distance:20] of boiling water.

**Source:** `= this.source` (`= this.source-type`)
