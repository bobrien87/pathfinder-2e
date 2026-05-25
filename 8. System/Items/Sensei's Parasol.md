---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]", "[[Monk]]", "[[Parry]]", "[[Reach]]", "[[Trip]]"]
price: "{'gp': 1400}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A master once said to his pupil that, in the hands of a skilled practitioner, even a parasol can become a deadly weapon. Returning the next day, the pupil excitedly turned over a parasol forged out of metal slats, explaining that it lowered the amount of skill one would need to exert deadly force. The master sighed, seeing that his pupil had failed to see the point, but accepted the gift nonetheless. Ingenuity was, after all, a virtue.

Since then, other smiths have imitated the pupil's design and crafted additional sensei's parasols, and they're highly sought after by those who appreciate multipurpose tools. This weapon functions as a +2 striking bo staff.

**Activate—Your Attacks Are but Raindrops** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You cause the metal slats of the parasol to open up, transforming it into a moderate sturdy shield (Hardness 13, HP 104 [BT 51]). You can sustain this activation for up to 10 minutes, after which the sensei's parasol reverts back to bo staff form. If it's broken as a shield, it reverts to its undamaged bo staff form. If it's destroyed as a shield, it reverts to bo staff form and becomes broken.

**Activate—Defensive Redirection** `pf2:r` (concentrate)

**Requirements** The sensei's parasol is in bo staff form and isn't broken

**Frequency** once per day

**Trigger** A creature misses you with a melee Strike

**Effect** You redirect the missed Strike to target a creature or object within the triggering creature's reach. The triggering creature rolls a new Strike against the new target to determine the results of the redirected attack.

**Source:** `= this.source` (`= this.source-type`)
