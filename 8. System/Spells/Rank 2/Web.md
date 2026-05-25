---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "30 feet"
area: "10-foot burst"
defense: "Reflex"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a sticky web in the area that impedes creatures' movement. Squares filled with the web are difficult terrain. Each time a creature in the web begins to use a move action or enters the web during a move action it's using, it must attempt an [[Athletics]] check or Reflex save against your spell DC to avoid taking a circumstance penalty to its Speeds or becoming [[Immobilized]]. A creature that gets out of the web ceases to take a circumstance penalty to its Speed from the web. Each square can be cleared of the web by a single attack or effect that deals at least 5 slashing damage or 1 fire damage. A square has AC 5, and it automatically fails its saving throws.
- **Critical Success** The creature is unaffected, and it doesn't need to attempt further Athletics checks or saving throws against the web this turn. If it used an Athletics check, it clears the web from every square it leaves during its movement.
- **Success** The creature is unaffected during its action. If it used an Athletics check, it clears the web from every square it leaves during its movement.
- **Failure** The creature takes a –10-foot circumstance penalty to its Speeds until the start of its next turn.
- **Critical Failure** The creature is immobilized until the start of its next turn, after which it takes a –10-foot circumstance penalty to its Speeds for 1 round. It can attempt to [[Escape]] to remove its immobilized condition.

**Heightened (4th)** The spell's area increases to a @Template[burst|distance:20], and its range increases to 60 feet.

**Source:** `= this.source` (`= this.source-type`)
