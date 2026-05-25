---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]"]
price: "{'gp': 459}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This top has 20 divisions, painted in a chaotic mess of clashing colors. When spun, the top quickly settles on a side and generates a strange magical effect based on the side that lands face-up.

**Activate—Spin the Top** `pf2:2` (concentrate, manipulate)

**Effect** Choose a creature within 60 feet to target and roll a d20 on the table below to determine the top's effect. You make any decisions for a spell cast by the top unless otherwise indicated, except that it must target the creature you chose, or the creature you chose must be the center of the spell's area, if it has an area but no targets. If the spell's range is less than 60 feet, increase the range to 60 feet.

Any spell DC required is DC 27, and any spell attack roll required is +17. If the top casts a spell on you, you don't get a saving throw or other defense against it.

The top can't be activated again for 1d4 hours

[[Madcap Top Effect]]

d20Madcap Top Effect1You spin just like the top. You are [[Stunned]] for 1 round and then [[Confused]] for 1 round.2[[Slow]] affects the target.3[[Shrink]] affects you for 1 day.4A 3rd-rank [[Illusory Disguise]] makes you look like the target.5A statue of the target, made of chocolate or candy, appears adjacent to you.6Gravity reverses, sending you and the target 30 feet in the air, immobilized. You both fall at the start of your next turn.7[[Mind Reading]] affects the target, and the top loudly recites what it discovers.8[[Laughing Fit]] affects the target.9A fountain erupts from the top, spraying wine for 10 minutes.10[[Translocate]] affects you, but you teleport through Hell.11[[Invisibility]] affects you.12Four singing skeletons appear to serenade you and your allies for 1 minute, granting a +1 status bonus to attack rolls, Perception checks, saving throws, and skill checks.13The top flings 1 cp at you.14[[Confusion]] affects the target.15You and the target change places; this is a teleportation effect.16[[Banishment]] affects the target, or paralyze if the target's on its home plane.17Rainbow dye explodes and covers you for 24 hours.18The top creates a [[Toxic Cloud]] centered on the target.19A random unattended object within 60 feet of you sprouts animal legs and follows you, reverting when the top's activation recharges.20Spin again, and the target also spins as though it had activated the top.

**Source:** `= this.source` (`= this.source-type`)
