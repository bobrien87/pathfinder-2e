---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Druid]]", "[[Focus]]"]
cast: "`pf2:0`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You enhance a summoned creature with the power of the elements. If your next action is to cast either [[Summon Animal]] or [[Summon Plant or Fungus]], choose air, earth, fire, metal, water or wood; the creature you summon gains the corresponding abilities.

- **Air** The creature gains a fly Speed of 60 feet.

- **Earth** The creature gains a burrow Speed of 20 feet, reduces its land Speed by 10 feet (minimum 5 feet), and gains resistance 5 to physical damage.

- **Fire** The creature's Strikes deal 1d6 extra fire damage, and it gains resistance 10 to fire and weakness 5 to cold and water.

- **Metal** The creature's Strikes deal 1d6 extra electricity damage, and it gains resistance 5 to electricity.

- **Water** The creature gains a swim Speed of 60 feet, can spend 1 action after a melee attack to attempt a Shove (ignoring multiple attack penalty), and gains resistance 5 to fire.

- **Wood** The creature gains a climb speed of 30 feet and resistance 2 to bludgeoning and piercing damage.

> [!danger] Effect: Spell Effect: Primal Summons

**Source:** `= this.source` (`= this.source-type`)
