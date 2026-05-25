---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Misfortune]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "1 minute (see text)"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a spectral albatross, a guiding bird for sailors, to hover around the target. You and allies within 30 feet of the target gain a +1 circumstance bonus to attacks against the target. The target creature can spend an action to Strike the albatross, which automatically succeeds and kills it. The target must then attempt a Will save against your spell DC.

> [!danger] Effect: Spell Effect: Albatross Curse
- **Critical Success** The target is unaffected.
- **Success** The guilt of slaughtering a bird of good fortune weighs on the target's mind. The target is [[Stupefied 1]] for 1 round.
- **Failure** The albatross hangs around a cord from the target's neck (or closest equivalent) for 1 minute, cursing them for their transgression. During this time, the target must roll twice and take the worse result on their next Will save, after which the albatross disappears.

> [!danger] Effect: Spell Effect: Albatross Curse (Failure)
- **Critical Failure** As failure, but the duration is 1 hour.

> [!danger] Effect: Spell Effect: Albatross Curse (Critical Failure)

**Source:** `= this.source` (`= this.source-type`)
