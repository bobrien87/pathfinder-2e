---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Metal]]", "[[Poison]]"]
cast: "`pf2:2`"
range: "60 feet"
area: "20-foot burst"
defense: "basic Fortitude"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

This spell forces toxic metal to coalesce on the skin or surface of all living creatures in the area, dealing 4d6 poison damage with a basic Fortitude save. Any creature that has the plant trait, has the wood trait, or has an anathema toward metal, takes the following effects depending on the result of that Fortitude save.
- **Critical Success** The creature suffers no additional effects.
- **Success** The creature takes 1 persistent,poison damage and is [[Sickened]] 1 as long as it takes this persistent damage.
- **Failure** As success, except 1d4 persistent,poison damage and [[Sickened]] 2.
- **Critical Failure** As success, except 1d8 persistent,poison damage and [[Sickened]] 3.

**Heightened (+1)** The initial poison damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
