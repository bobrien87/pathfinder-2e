---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Polymorph]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call upon primal energy to transform yourself into a Medium animal battle form. When you Cast this Spell, choose a listed battle form. You can decide the specific type of animal (such as lion or snow leopard for cat), but this has no effect on the form's Size or statistics. While in this form, you gain the animal trait. You can Dismiss the spell.

You gain the following statistics and abilities regardless of which animal you choose:

- AC = 16 + your level. Ignore your armor's check penalty and Speed reduction.
- 5 temporary Hit Points.
- Low-light vision and imprecise scent 30 feet.
- One or more unarmed melee attacks specific to your battle form, which are the only attacks you can Strike with. You're trained with them. Your attack modifier is +9, and your damage bonus is +1. These attacks are Strength based (for the purpose of the [[Enfeebled]] condition, for example). If your unarmed attack bonus is higher, you can use it instead.
- Athletics modifier of +9, unless your own modifier is higher.

You also gain specific abilities based on the type of animal you choose:

- **

> [!danger] Effect: Ape

**

- Speed 25 feet, climb Speed 20 feet;
- **Melee** a fist, **Damage** 2d6 bludgeoning.

- **

> [!danger] Effect: Bear

**

- Speed 30 feet;
- **Melee** a jaws, **Damage** 2d8 piercing;
- **Melee** a claw (agile), **Damage** 1d8 slashing.

- **

> [!danger] Effect: Bull

**

- Speed 30 feet;
- **Melee** a horn, **Damage** 2d8 piercing.

- **

> [!danger] Effect: Canine

**

- Speed 40 feet;
- **Melee** a jaws, **Damage** 2d8 piercing.

- **

> [!danger] Effect: Cat

**

- Speed 40 feet;
- **Melee** a jaws, **Damage** 2d6 piercing;
- **Melee** a claw (agile), **Damage** 1d10 slashing.

- **

> [!danger] Effect: Crab

**

- Speed 25 feet, swim Speed 15 feet;
- **Melee** a big claw, **Damage** 2d8 piercing;
- **Melee** a little claw (agile), **Damage** 2d4 piercing.

- **

> [!danger] Effect: Crocodile

**

- Speed 25 feet, swim Speed 30 feet;
- **Melee** a jaws, **Damage** 2d8 piercing;
- **Melee** a tail (agile), **Damage** 1d8 bludgeoning.
- can hold your breath for the duration of the transformation.

- **

> [!danger] Effect: Deer

**

- Speed 50 feet;
- **Melee** a antler, **Damage** 2d6 piercing.

- **

> [!danger] Effect: Frog

**

- Speed 25 feet, swim Speed 25 feet;
- **Melee** a jaws, **Damage** 2d6 bludgeoning;
- **Melee** a tongue (reach 15 feet), **Damage** 2d4 bludgeoning.

- **

> [!danger] Effect: Orca

**

- swim Speed 35 feet;
- **Melee** a jaws, **Damage** 2d8 piercing;
- can hold your breath for the duration of the transformation.

- **

> [!danger] Effect: Seal

**

- Speed 20 feet, swim Speed 30 feet;
- **Melee** a jaws (grapple), **Damage** 2d6 piercing;
- can hold your breath for the duration of the transformation.

- **

> [!danger] Effect: Shark

**

- swim Speed 35 feet;
- **Melee** a jaws, **Damage** 2d8 piercing;
- breathe underwater but not in air.

- **

> [!danger] Effect: Snake

**

- Speed 20 feet, climb Speed 20 feet, swim Speed 20 feet;
- **Melee** a fangs, **Damage** 2d4 piercing plus 1d6 poison.

**Heightened (3rd)** You instead gain 10 temporary HP, AC = 17 + your level, attack modifier +14, damage bonus +5, and Athletics +14.

**Heightened (4th)** Your battle form is Large and your attacks have 10-foot reach. You must have enough space to expand into or the spell is lost. You instead gain 15 temporary HP, AC = 18 + your level, attack modifier +16, damage bonus +9, and Athletics +16.

**Heightened (5th)** Your battle form is Huge and your attacks have 15-foot reach. You must have enough space to expand into or the spell is lost. You instead gain 20 temporary HP, AC = 18 + your level, attack modifier +18, damage bonus +7 and double the number of damage dice, and Athletics +20.

**Source:** `= this.source` (`= this.source-type`)
