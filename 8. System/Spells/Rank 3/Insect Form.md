---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Polymorph]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You envision a simple bug and transform into a Medium animal battle form. When you Cast this Spell, choose a listed battle form. You can decide the specific type of animal (such as a ladybug or scarab for beetle), but this has no effect on the form's Size or statistics. While in this form, you gain the animal trait. You can Dismiss this spell.

You gain the following statistics and abilities regardless of which battle form you choose:

- AC = 18 + your level. Ignore your armor's check penalty and Speed reduction.
- 10 temporary Hit Points.
- Low-light vision.
- One or more attacks specific to the battle form you choose, which are the only attacks you can Strike with. You're trained with them. Your attack modifier is +13, and your damage bonus is +2. These attacks are Strength based (for the purpose of the [[Enfeebled]] condition). If your unarmed attack modifier is higher, you can use it instead.
- Athletics modifier of +13, unless your own is higher.

You also gain specific abilities based on the form you choose:

- **

> [!danger] Effect: Ant

**

- Speed 30 feet, climb Speed 30 feet;
- **Melee** `pf2:1` mandibles, **Damage** 2d6 bludgeoning.

- **

> [!danger] Effect: Beetle

**

- Speed 25 feet;
- **Melee** `pf2:1` mandibles, **Damage** 2d10 bludgeoning.

- **

> [!danger] Effect: Centipede

**

- Speed 25 feet, climb Speed 25 feet; darkvision;
- **Melee** `pf2:1` mandibles, **Damage** 1d8 piercing plus 1d4 persistent poison.

- **

> [!danger] Effect: Mantis

**

- Speed 40 feet; imprecise scent 30 feet;
- **Melee** `pf2:1` foreleg, **Damage** 2d8 piercing.

- **

> [!danger] Effect: Scorpion

**

- Speed 40 feet; darkvision, imprecise tremorsense 60 feet;
- **Melee** `pf2:1` stinger, **Damage** 1d8 piercing plus 1d4 persistent poison;
- **Melee** `pf2:1` pincer (agile), **Damage** 1d6 bludgeoning.

- **

> [!danger] Effect: Spider

**

- Speed 25 feet, climb Speed 25 feet; darkvision;
- **Melee** `pf2:1` fangs, **Damage** 1d6 piercing plus 1d4 persistent poison;
- **Ranged** `pf2:1` web (range increment 20 feet), **Damage** [[immobilizes]] the target for 1 round or until it Escapes..

**Heightened (4th)** Your battle form is Large, and your attacks have 10-foot reach. You instead gain 15 temporary HP, attack modifier +16, damage bonus +6, and Athletics +16.

**Heightened (5th)** Your battle form is Huge, and your attacks have 15-foot reach. You instead gain 20 temporary HP, attack modifier +18, damage bonus +2 and double damage dice (including persistent damage), and Athletics +20.

**Source:** `= this.source` (`= this.source-type`)
