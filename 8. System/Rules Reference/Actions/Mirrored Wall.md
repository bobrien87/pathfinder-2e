---
type: action
source-type: "Remaster"
traits: ["[[Commander]]", "[[Tactic]]", "[[Visual]]"]
cast: "`pf2:2`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per 10 minutes

**Requirements** At least one of your squadmates is in bright light or has a focused light source available, such as a bull's-eye lantern.

Your squadmates have polished their shields to a reflective sheen and now position them to reflect a blinding light into your enemy's eyes. All of your squadmates can Raise a Shield or cast [[Shield]] as a reaction.

Then, signal a squadmate within the aura of your commander's banner who currently has a shield raised (including spellcasting allies with an active casting of the *shield* cantrip), and choose an enemy within 60 feet. The formation bounces light off the raised shield and into the enemy's eyes; the target must succeed at a [[Fortitude]] save saving throw against your class DC or become [[Blinded]] for 1 round (on a critical failure, the creature remains [[Dazzled]] for 3 rounds after the blindness ends).

You can signal additional allies with raised shields to participate in this tactic; the target takes a circumstance penalty on this save equal to the number of additional participating squadmates (to a maximum –4 circumstance penalty to the target's save).

> [!danger] Effect: Mirrored Wall

**Source:** `= this.source` (`= this.source-type`)
