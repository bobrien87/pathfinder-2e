---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Manipulate]]", "[[Mental]]", "[[Misfortune]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 creature"
defense: "Will"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You afflict the target with a curse that makes its presence abrasive and off-putting. The target must attempt a Will save.
- **Critical Success** The target is unaffected.
- **Success** For 10 minutes, the target must roll twice and use the worse result whenever attempting a Deception, Diplomacy, Intimidation, or Performance check, and creatures they encounter have an initial attitude toward them of one step worse (for instance, [[Unfriendly]] instead of [[Indifferent]]).

> [!danger] Effect: Spell Effect: Outcast's Curse (Success)
- **Failure** As success, but the effect is permanent.

> [!danger] Effect: Spell Effect: Outcast's Curse (Failure)
- **Critical Failure** As failure, and creatures that the target encounters have an initial attitude toward them of two steps worse.

**Source:** `= this.source` (`= this.source-type`)
