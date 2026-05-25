---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Fungus]]", "[[Manipulate]]", "[[Poison]]"]
cast: "`pf2:2`"
range: "touch"
area: "15-foot cone"
defense: "Fortitude"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Toxic spores swarm over creatures in the area, causing them to erupt in grotesque fungal growths. These noxious growths deal 2d6 persistent poison damage, and each creature must attempt a Fortitude save.
- **Critical Success** The creature is unaffected.
- **Success** The target takes half the persistent poison damage.
- **Failure** The target takes the full persistent poison damage. While it's taking this persistent poison damage, it has weakness 1 to fire and weakness 1 to slashing.
- **Critical Failure** As failure, but double the persistent poison damage. While it's taking this persistent poison damage, it has weakness 2 to fire and weakness 2 to slashing.

> [!danger] Effect: Spell Effect: Fungal Infestation

**Heightened (+2)** The persistent damage increases by 2d6, and the weakness increases by 1, or by 2 on a critical failure.

**Source:** `= this.source` (`= this.source-type`)
