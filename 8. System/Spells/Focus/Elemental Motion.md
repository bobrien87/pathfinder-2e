---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Sorcerer]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call upon your element to propel you, improving your Speed depending on your element. This spell has your element's trait.

- **Air** You gain a fly Speed equal to your Speed.
- **Earth** You gain a burrow Speed of 10 feet.
- **Fire** You gain a fly Speed equal to your Speed.
- **Metal** You gain a burrow Speed of 10 feet.
- **Water** You gain a swim Speed equal to your Speed and can breathe underwater.
- **Wood** You gain a climb Speed equal to your Speed.

> [!danger] Effect: Spell Effect: Elemental Motion

**Heightened (6th)** You also gain a +10-foot status bonus to your Speeds.

**Heightened (9th)** The status bonus increases to +20 feet.

**Source:** `= this.source` (`= this.source-type`)
