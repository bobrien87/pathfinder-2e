---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Morph]]", "[[Ranger]]"]
cast: "`pf2:1`"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Without fully transforming your body, you gain one animalistic feature, which you select from the list below each time you Cast the Spell.

- **Cat Eyes** You gain low-light vision.

- **Claws** You gain a claw attack that deals 1d6 slashing damage and has the agile, finesse, and unarmed traits.

- **Jaws** You gain a jaws attack that deals 1d8 piercing damage and has the unarmed trait.

**Heightened (4th)** Add the following options to the list.

- **Fish Tail** You gain a swim Speed equal to your land Speed.

- **Owl Eyes** You gain darkvision.

- **Wings** You gain a fly Speed equal to your land Speed.

> [!danger] Effect: Spell Effect: Animal Feature

**Source:** `= this.source` (`= this.source-type`)
