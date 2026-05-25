---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 object held by 1 creature and the creature holding it"
defense: "Reflex"
duration: "varies"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

One object held by a creature becomes fused to that creature's hand and can't be put down. To [[Disarm]] or [[Steal]] the item, the result of the skill check must exceed the spell's DC or the normal DC, whichever is higher. To voluntarily drop the weapon, the target must spend an Interact action rather than a free action, and then succeed at a Reflex save; the target must also attempt a Reflex save to Interact to put away or swap the object. On a failed save, the action is wasted, but on a success, they drop the item and the spell ends. An unwilling creature must attempt an initial Reflex save against lock item. A willing creature can choose to critically fail the saving throw.
- **Critical Success** The creature is unaffected.
- **Success** The creature is affected for 1 round.
- **Failure** The creature is affected for 4 rounds.
- **Critical Failure** The creature is affected for 1 minute.

**Heightened (+2)** You can target either one additional object held by the same creature or one additional object held by one additional creature.

**Source:** `= this.source` (`= this.source-type`)
