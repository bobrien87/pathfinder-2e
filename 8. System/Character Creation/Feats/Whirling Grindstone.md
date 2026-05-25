---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Attack]]", "[[Composite]]", "[[Earth]]", "[[Impulse]]", "[[Kineticist]]", "[[Metal]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A whirling grindstone made of flint appears in an unoccupied square within 30 feet. The grindstone shreds flesh and shoots sparks. Attempt an Impulse check{impulse attack} roll against the AC of a creature adjacent to the grindstone. On a hit, the creature takes @Damage[(floor((@actor.level -4)/5)+2)d6[slashing], (floor((@actor.level -4)/5)+1)d6[fire]] damage (or double damage on a critical hit). The grindstone lasts until the end of your next turn, and you can Sustain the impulse up to 1 minute. On subsequent turns, the first time you Sustain the impulse that turn, you can roll the grindstone up to 20 feet and can repeat the attack.

A creature within reach of the grindstone can Interact with it to sharpen a metal weapon. This grants a +2 circumstance bonus to the next damage roll made with that weapon within 1 minute.

**Level (+5)** The grindstone's damage increases by 1d6 slashing and 1d6 fire, and the bonus to weapons increases by 1.

**Source:** `= this.source` (`= this.source-type`)
