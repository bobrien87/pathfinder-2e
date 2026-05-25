---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Polymorph]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You harness your mastery of primal forces to reshape your body into a Medium flying animal battle form. When you Cast this Spell, choose a listed battle form. You can decide the specific type of animal (such as an owl or eagle for bird), but this has no effect on the form's Size or statistics. While in this form, you gain the animal trait. You can Dismiss the spell.

You gain the following statistics and abilities regardless of which battle form you choose:

- AC = 18 + your level. Ignore your armor's check penalty and Speed reduction.

- 5 temporary Hit Points.

- Low-light vision.

- One or more unarmed melee attacks specific to the battle form you choose, which are the only attacks you can Strike with. You're trained with them. Your attack modifier is +16, and your damage bonus is +5. These attacks are Dexterity based (for the purpose of the [[Clumsy]] condition, for example). If your attack modifier for Dexterity-based unarmed attacks is higher, you can use it instead.

- Acrobatics modifier of +16, unless your own modifier is higher.

You also gain specific abilities based on the form you choose:

- **

> [!danger] Effect: Bat

**

- Speed 20 feet, fly Speed 30 feet; precise echolocation 40 feet;

- **Melee** a fangs, **Damage** 2d8 piercing;

- **Melee** a wing (agile), **Damage** 2d6 bludgeoning.

- **

> [!danger] Effect: Bird

**

- Speed 10 feet, fly Speed 50 feet;

- **Melee** a beak, **Damage** 2d8 piercing;

- **Melee** a talon (agile), **Damage** 1d10 slashing.

- **

> [!danger] Effect: Pterosaur

**

- Speed 10 feet, fly Speed 40 feet; imprecise scent 30 feet;

- **Melee** a beak, **Damage** 3d6 piercing.

- **

> [!danger] Effect: Wasp

**

- Speed 20 feet, fly Speed 40 feet;

- **Melee** a stinger, **Damage** 1d8 piercing plus 1d6 persistent poison.

**Heightened (5th)** Your battle form is Large and your fly Speed gains a +10-foot status bonus. You must have enough space to expand into or the spell is lost. You instead gain 10 temporary HP, attack modifier +18, damage bonus +8, and Acrobatics +20.

**Heightened (6th)** Your battle form is Huge, your fly Speed gains a +15-foot status bonus, and your attacks have 10-foot reach. You must have enough space to expand into or the spell is lost. You instead gain AC = 21 + your level, 15 temporary HP, attack modifier +21, damage bonus +4 and double damage dice (including persistent damage), and Acrobatics +23.

**Source:** `= this.source` (`= this.source-type`)
