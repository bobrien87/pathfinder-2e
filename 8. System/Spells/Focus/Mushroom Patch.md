---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Druid]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "60 feet"
area: "10-foot burst"
defense: "Fortitude"
duration: "1 minute"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cause mushrooms to sprout in the area. The area becomes difficult terrain. When the spell is cast and at the beginning of each round, the mushroom's release a cloud of irritating spores. Creatures in the area must attempt a Fortitude save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Dazzled]] for 1 round. If the creature moves to outside area, they can spend 1 action to rub their eyes, removing the dazzled condition.
- **Failure** The creature becomes dazzled for 1 round.
- **Critical Failure** The creature becomes dazzled and [[Slowed]] 1 for 1 round.

**Heightened (3rd)** The range increases to 90 feet and the area increases to a 20-foot-radius burst.

**Heightened (6th)** The range increases to 120 feet and the area increases to a 30-foot-radius burst.

**Heightened (9th)** The range increases to 150 feet, the area increases to a 40-foot-radius burst, and when a creature would become dazzled, they become [[Blinded]] instead.

**Source:** `= this.source` (`= this.source-type`)
