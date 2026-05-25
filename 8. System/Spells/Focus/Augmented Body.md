---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Morph]]", "[[Wizard]]"]
cast: "`pf2:1`"
duration: "1 minute"
source: "Pathfinder #215: To Blot Out the Sun"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You magically augment your body with clockwork parts and magitech innovations. Choose any one effect of your choice. You can Dismiss the spell.

- **Ablative Plating** You coat your body with metal plates that protect your vital organs. You gain resistance 1 to physical damage.
- **Clockwork Arm** You transform one of your arms into a clockwork arm powered by gears, springs, and pneumatic actuators. You gain a clockwork fist unarmed attack, which has the agile, finesse, and free-hand traits and deals 1d6 bludgeoning damage.
- **Spined Fingertips** Your fingers sprout microscopic metal spines that enable you to cling to surfaces like a spider. You gain a climb Speed of 20 feet.
- **Spring-Loaded Legs** Your leg muscles are augmented with powerful springs. You gain a +10-foot status bonus to your Speed and double the distance you [[Leap]].

> [!danger] Effect: Spell Effect: Augmented Body

**Heightened (3rd)** The ablative plating's resistance increases to 2. The clockwork fist is a +1 striking weapon.

**Heightened (5th)** The ablative plating's resistance increases to 3, and the clockwork fist is a +2 striking weapon.

**Heightened (7th)** The ablative plating's resistance increases to 4, and the clockwork fist is a +2 greater striking weapon.

**Heightened (9th)** The ablative plating's resistance increases to 5 and the clockwork fist is a +3 major striking weapon.

**Source:** `= this.source` (`= this.source-type`)
