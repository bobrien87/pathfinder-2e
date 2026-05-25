---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Polymorph]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call upon the power of the planes to transform into a Medium elemental battle form. When you Cast this Spell, choose a listed element. While in this form, you gain the corresponding trait and the elemental trait. You have hands in this battle form and can take manipulate actions. You can Dismiss the spell.

You gain the following statistics and abilities regardless of which battle form you choose:

- AC = 19 + your level. Ignore your armor's check penalty and Speed reduction.

- 10 temporary Hit Points.

- Darkvision.

- One or more unarmed melee attacks specific to the battle form you choose, which are the only attacks you can Strike with. You're trained with them. Your attack modifier is +18, and your damage bonus is +9. These are Dexterity based (air, fire, or metal) or Strength based (earth, water, or wood). If your corresponding unarmed attack modifier is higher, you can use it instead.

- Acrobatics (air, fire, or metal) or Athletics (earth, water, or wood) modifier of +20; ignore this change if your own modifier is higher.

You also gain specific abilities based on the type of elemental you choose:

- **Air**

- fly 80 feet, movement doesn't trigger reactions;

- **Melee** `pf2:1` gust, **Damage** 1d4 bludgeoning.

- **Earth**

- Speed 20 feet, burrow 20 feet;

- **Melee** `pf2:1` boulder, **Damage** 2d10 bludgeoning.

- **Fire**

- Speed 50 feet; fire resistance 10, weakness 5 to cold and 5 to water;

- **Melee** `pf2:1` tendril, **Damage** 1d8 fire plus 1d4 persistent fire.

- **Metal**

- Speed 40 feet, fly 20 feet;

- **Melee** `pf2:1` blade (versatile piercing), **Damage** 1d8 slashing plus 1d4 electricity.

- **Water**

- Speed 20 feet, swim 60 feet; fire resistance 5;

- **Melee** `pf2:1` wave, **Damage** 1d12 bludgeoning, and you can spend an action immediately after a hit to push the target 5 feet with the effects of a successful [[Shove]].

- **Wood**

- Speed 20 feet, climb 30 feet;

- **Melee** `pf2:1` branch, **Damage** 2d10 bludgeoning.

**Heightened (6th)** Your battle form is Large and your attacks have 10-foot reach. You must have space to expand or the spell is lost. You instead gain AC = 22 + your level, 15 temporary HP, an attack modifier of +23, a damage bonus of +13, and Acrobatics or Athletics +23.

**Heightened (7th)** Your battle form is Huge and your attacks have 15-foot reach. You must have space to expand or the spell is lost. You instead gain AC = 22 + your level, 20 temporary HP, an attack modifier of +25, a damage bonus of +11, double the number of damage dice (including persistent damage), and Acrobatics or Athletics +25.

> [!danger] Effect: Spell Effect: Elemental Form

**Source:** `= this.source` (`= this.source-type`)
