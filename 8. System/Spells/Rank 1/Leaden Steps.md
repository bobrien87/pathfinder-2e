---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Metal]]", "[[Morph]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Fortitude"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You partially transform a foe's feet into unwieldy slabs of metal, slowing their steps. The target attempts a Fortitude saving throw.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Encumbered]] and has weakness 2 to electricity until the end of your next turn. The spell can't be sustained.
- **Failure** The target is encumbered and has weakness 2 to electricity.
- **Critical Failure** The target is encumbered and has weakness 3 to electricity.

> [!danger] Effect: Spell Effect: Leaden Steps

**Heightened (+1)** The weakness increases by 1.

**Source:** `= this.source` (`= this.source-type`)
