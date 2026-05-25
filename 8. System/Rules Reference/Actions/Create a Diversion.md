---
type: action
source-type: "Remaster"
traits: ["[[Mental]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

With a gesture, a trick, or some distracting words, you can create a diversion that draws creatures' attention elsewhere. If you use a gesture or trick, this action gains the manipulate trait. If you use distracting words, it gains the auditory and linguistic traits.

Attempt a single Deception check and compare it to the Perception DCs of the creatures whose attention you're trying to divert. Whether or not you succeed, creatures you attempt to divert gain a +4 circumstance bonus to their Perception DCs against your attempts to Create a Diversion for 1 minute.
- **Success** You become [[Hidden]] to each creature whose Perception DC is less than or equal to your result. (The hidden condition allows you to [[Sneak]] away.) This lasts until the end of your turn or until you do anything except Step or use the Stealth skill to Hide or Sneak. If you Strike a creature, the creature remains [[Off Guard]] against that attack, and you then become observed. If you do anything else, you become observed just before you act unless the GM determines otherwise.
- **Failure** You don't divert the attention of any creatures whose Perception DC exceeds your result, and those creatures are aware you were trying to trick them.

**Source:** `= this.source` (`= this.source-type`)
