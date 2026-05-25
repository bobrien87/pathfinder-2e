---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "10"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Polymorph]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Drawing upon the deepest wells of magic in an elemental plane, you transform into a spectacular elemental. You can choose between an air elemental, earth elemental, fire elemental, or water elemental. Your battle form is Gargantuan, and you must have enough space to expand into or the spell is lost. While in this form, you gain the elemental trait and the trait for the element you choose. You can Dismiss the spell.

You gain the following statistics and abilities regardless of which battle form you choose:

- AC = 25 + your level. Ignore your armor's check penalty and Speed reduction.
- 30 temporary Hit Points.
- Darkvision.
- One or more attacks specific to the battle form you choose, which are the only attacks you can Strike with. You're trained with them. Your attack modifier is +34, and you use the listed damage. These attacks are Dexterity based if you choose an air or fire elemental, or Strength based if you choose an earth or water elemental. (This distinction doesn't change the statistics, but matters for the enfeebled and clumsy conditions, for example). If your unarmed attack modifier is higher, you can use it instead.
- Acrobatics modifier of +36 for air or fire elemental or Athletics modifier of +36 for earth or water elemental, unless your own modifier is higher.

You also gain specific abilities based on the type of elemental you choose:

- **

> [!danger] Effect: Air Elemental

** fly Speed 80 feet;

- **High Winds** (air, aura) 30 feet. Air within the emanation is difficult terrain for flying creatures that don't have the air trait;
- **Swiftness** Your movement doesn't trigger reactions;
- **Melee** `pf2:1` gust (reach 25 feet), **Damage** 3d12+11 bludgeoning plus Push 10 feet;
- **Ranged** `pf2:1` lightning lash (range increment 80 feet), **Damage** 3d12+4 electricity.

- **

> [!danger] Effect: Earth Elemental

** 30 feet, burrow 20 feet; resistance 5 to physical;

- **Spike Stones** (aura, earth) 30 feet. The area is difficult terrain and hazardous terrain. A creature without the earth trait that moves on the ground in the area takes 5 piercing damage for every square of that area it moves into;
- **Rocky Toughness** You gain 40 temporary Hit Points when you choose this form instead of 30;
- **Melee** `pf2:1` fist (reach 25 feet), **Damage** 3d12+15 bludgeoning;
- **Ranged** `pf2:1` rock (range increment 40 feet), **Damage** 4d8+6 bludgeoning.

- **

> [!danger] Effect: Fire Elemental

** 50 feet; immunity to fire; weakness to cold 10;

- **Intense Heat** (aura, fire) 30 feet. A creature that enters the aura or starts its turn in the aura takes 5d6 fire damage with a basic Reflex save against your spell DC. A creature can take damage from the aura only once per round;
- **Melee** `pf2:1` tendril (reach 25 feet), **Damage** 3d10+12 fire plus 2d6 persistent fire;
- **Ranged** `pf2:1` fire mote (range increment 60 feet), **Damage** 4d8+6 fire.

- **

> [!danger] Effect: Metal Elemental

** 40 feet, fly 40 feet; resistance 10 to electricity;

- **Arcing Electricity** (aura, electricity, metal) 30 feet. A creature that enters the aura or starts its turn in the aura takes 2d12 electricity damage with a basic Reflex save against your spell DC; a creature made of metal, with the metal trait, or wearing metal armor takes a –1 circumstance penalty on this save. A creature can take damage from the aura only once per round;
- **Melee** `pf2:1` blade (reach 25 feet, versatile slashing), **Damage** 3d12+15 piercing;
- **Ranged** `pf2:1` metal shard (range increment 40 feet, versatile slashing), **Damage** 4d8+6 piercing.

- **

> [!danger] Effect: Water Elemental

** 40 feet, swim 80 feet; resistance 10 to fire;

- **Vortex** (aura, water) 30 feet. Water within the aura that is part of the same body of water you occupy is difficult terrain for Swimming creatures that don't have the water trait;
- **Melee** `pf2:1` wave (reach 25 feet), **Damage** 3d12+18 bludgeoning plus Push or Pull 10 feet;
- **Ranged** `pf2:1` water spout (range increment 60 feet), **Damage** 4d8+6 bludgeoning.

- **

> [!danger] Effect: Wood Elemental

** 30 feet, climb 35 feet; resistance 5 to physical; weakness to axes 10;

- **Lush Growth** (aura, wood) 30 feet. Ground in the area is difficult terrain, and any time a creature in the area regains HP from a healing vitality effect, the aura grants a +5 status bonus to the healing;
- **Woody Toughness** You gain 40 temporary Hit Points when you choose this form instead of 30;
- **Melee** `pf2:1` branch (reach 25 feet), **Damage** 3d10+18 piercing;
- **Ranged** `pf2:1` seed (range increment 40 feet), **Damage** 4d8+6 bludgeoning.

**Source:** `= this.source` (`= this.source-type`)
