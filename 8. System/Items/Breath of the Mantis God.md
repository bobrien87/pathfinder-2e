---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Inhaled]]", "[[Poison]]", "[[Virulent]]"]
price: "{'gp': 200}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

To prevent one of their victims from being brought back to life, Red Mantis assassins often poison targets with the breath of the mantis god. After a creature is poisoned by this concoction, internal hemorrhaging frequently results in blood issuing from the creature's mouth—a condition referred to by the assassins as having "the breath of the mantis god." While a creature can attempt to recover normally from the persistent bleed damage caused by breath of the mantis god, the persistent bleed damage will return if the poison's duration is still ongoing. If a creature dies from the poison's effects, the toxin lingers tenaciously in the creature's flesh for 1 year. During this time, if an attempt is made to bring such a slain creature back to life that doesn't create a new body for the deceased (such as with a 7th-rank [[Resurrect]] ritual), the lingering effects of breath of the mantis god attempts to counteract the resurrection (counteract modifier +17, counteract rank 5). A spell like [[Extract Poison]] can be used to decontaminate a corpse for easier resurrection, but simpler magic such as cleanse cuisine cannot. A 5th-rank or higher [[Cleanse Affliction]] can also attempt to counteract lingering breath of the mantis god.

**Saving Throw** DC 29 [[Fortitude]] save

**Maximum Duration** 6 minutes

**Stage 1** 3d6 bleed and [[Drained]] 1 (1 minute)

**Stage 2** 3d8 bleed and drained 1 (1 minute)

**Stage 3** 3d10 bleed and [[Drained]] 2 (1 minute)

**Source:** `= this.source` (`= this.source-type`)
