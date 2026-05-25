---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "2 or 3"
area: "60-foot cone"
defense: "basic Reflex"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You open a miniature portal to an elemental plane within your mouth, then exhale a powerful explosion of the plane's element. Roll 1d6 to determine the element. If you used 3 actions to Cast this Spell, you can choose the element instead. This spell gains the trait matching the element.

Each creature in the cone must attempt a basic Reflex save.

- **Air** Strong winds and lightning strikes buffet creatures in the cone, dealing 6d10 electricity damage. A creature that fails its save is also pushed 10 feet.

- **Earth** A cone of mud deals 5d10 bludgeoning damage to creatures in the area. A creature on the ground that fails its save slips and falls [[Prone]].

- **Fire** A surging cone of fire deals 7d10 fire damage.

- **Metal** A cone of rust slices flesh and damages metal. Each creature in the area takes 5d10 slashing damage. A creature made of metal gets a result one degree of success worse than it rolled, and an unattended metal object gets a critical failure.

- **Water** A torrent of chilled water deals 3d10 cold damage and 3d10 bludgeoning damage.

- **Wood** Branches rip through creatures, dealing 3d10 piercing damage and 3d10 slashing damage. Ground in the area becomes difficult terrain for 1 minute.

**Heightened (+1)** The damage increases by `r 1d10`. For water and wood, you can choose which damage type increases for each rank the spell is heightened.

**Source:** `= this.source` (`= this.source-type`)
