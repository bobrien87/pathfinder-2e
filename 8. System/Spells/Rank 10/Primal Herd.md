---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "10"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Polymorph]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "you and up to 5 willing targets"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Summoning the power of the natural world, you transform the targets into a herd of mammoths, and they each assume a Huge battle form. Each target must have enough space to expand into or the spell fails for that target. Each target gains the animal trait. Each target can Dismiss the spell's effects on itself. Each target gains the following while transformed.

- AC = 22 + the target's level. Ignore any armor check penalty and Speed reduction.

- 20 temporary Hit Points.

- Speed 40 feet.

- Low-light vision.

- The following unarmed melee attacks, which are the only attacks the target can use to Strike. When Striking with these attacks, the target uses their attack modifier with the proficiency and item bonuses of their most favorable weapon or unarmed Strike, and the damage is listed for each attack. These attacks are Strength based (for the purpose of the [[Enfeebled]] condition, for example).

- **Melee** `pf2:1` tusk (reach 15 feet), **Damage** 4d8+19 piercing
- **Melee** `pf2:1` trunk (agile, reach 15 feet), **Damage** 4d6+16 bludgeoning
- **Melee** `pf2:1` foot (agile, reach 15 feet), **Damage** 4d6+13 bludgeoning.

- Athletics modifier of +30, unless the target's own modifier is higher.

- Each target can use the Trample action.

- **Trample** `pf2:3` You move up to twice your Speed and move through the space of Large or smaller creatures, trampling each creature whose space you enter. A trampled creature takes damage from your foot Strike based on a basic Reflex save (DC = 19 + your level).

> [!danger] Effect: Spell Effect: Primal Herd

**Source:** `= this.source` (`= this.source-type`)
