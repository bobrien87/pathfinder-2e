---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "120 feet"
area: "15-foot burst"
defense: "Reflex"
duration: "1 minute"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You transmute the ground into a conical pit trap of loose sand that becomes difficult terrain for the duration. A creature or unsecured object that enters the sand or starts its turn in the sand is moved toward the center, depending on the result of its Reflex save. This is forced movement. If there isn't enough space near the center of the pit, affected creatures and objects move as far as they can without being blocked, up to the amount set by their saving throw outcomes.
- **Critical Success** The creature is unaffected.
- **Success** The creature moves 5 feet toward the center.
- **Failure** The creature moves 10 feet toward the center.
- **Critical Failure** As failure, and the creature becomes [[Immobilized]] in the pit. It can attempt to [[Escape]] against your spell DC.

**Heightened (+2)** Increase the area of the spell and the amount a creature moves on a failure by 5 feet.

**Source:** `= this.source` (`= this.source-type`)
