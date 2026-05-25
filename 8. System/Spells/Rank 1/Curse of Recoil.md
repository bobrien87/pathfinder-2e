---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Curse]]"]
cast: "`pf2:r`"
range: "120 feet"
targets: "1 creature"
defense: "Will"
duration: "1 round"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** An enemy you can see is about to make a ranged attack.

You curse an enemy to suffer a kickback as they make a ranged attack, potentially causing them to miss. The triggering enemy attempts a Will save.
- **Critical Success** The target is unaffected.
- **Success** The recoil from their ranged attack causes the target to be [[Off Guard]] until the beginning of their next turn.
- **Failure** The recoil imposes a –1 status penalty to the ranged attack and renders the target off-guard until the beginning of their next turn.

> [!danger] Effect: Spell Effect: Curse of Recoil (Failure)
- **Critical Failure** The recoil imposes a –2 status penalty to the ranged attack and renders the target off-guard until the beginning of their next turn. Until the start of their next turn, any additional ranged attacks made with the same weapon, spell, or ability take the same penalty.

> [!danger] Effect: Spell Effect: Curse of Recoil (Critical Failure)

**Source:** `= this.source` (`= this.source-type`)
