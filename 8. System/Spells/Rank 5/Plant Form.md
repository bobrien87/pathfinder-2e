---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Plant]]", "[[Polymorph]]", "[[Wood]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Taking inspiration from verdant creatures, you transform into a Large plant battle form. When you Cast this Spell, choose a listed battle form. You can substitute a similar specific plant to turn into (such as a pitcher plant instead of a flytrap), but this has no effect on the form's Size or statistics. While in this form, you gain the plant trait. You can Dismiss the spell.

You gain the following statistics and abilities regardless of which battle form you choose:

- AC = 19 + your level. Ignore your armor's check penalty and Speed reduction.

- 12 temporary Hit Points.

- Resistance 10 to poison.

- Low-light vision.

- One or more unarmed melee attacks specific to the battle form you choose, which are the only attacks you can Strike with. You're trained with them. Your attack modifier is +17, and your damage bonus is +11. These attacks are Strength based (for the purpose of the [[Enfeebled]] condition, for example). If your unarmed attack modifier is higher, you can use it instead.

- Athletics modifier of +19, unless your own modifier is higher.

You also gain specific abilities based on the type of plant you choose:

- **

> [!danger] Effect: Arboreal

**

- Speed 30 feet

- **Melee** `pf2:1` branch (reach 15 feet), **Damage** 2d10 bludgeoning;

- **Melee** `pf2:1` foot, **Damage** 2d8 bludgeoning;

- you can speak in this form

- **

> [!danger] Effect: Flytrap

**

- Speed 15 feet; resistance 10 to acid;

- **Melee** `pf2:1` leaf (reach 10 feet), **Damage** 2d8 piercing, and you can spend an action after a hit to Grab the target.

**Heightened (6th)** Your battle form is Huge, and the reach of your attacks increases by 5 feet. You instead gain AC = 22 + your level, 24 temporary HP, attack modifier +21, damage bonus +16, and Athletics +22.

**Source:** `= this.source` (`= this.source-type`)
