---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Oracle]]", "[[Polymorph]]"]
cast: "`pf2:2`"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your body becomes fluid to better suit your surroundings. Choose whether to become air, water, or mist. The spell gains the air trait if you choose air or mist, and the water trait if you choose water or mist. You become amorphous, as does your armor. You lose any item bonus to AC and use your proficiency bonus for unarmored defense to determine your AC. You also gain resistance 10 to physical damage and become immune to precision damage. You can slip through tiny cracks and don't need to breathe. You can't cast spells, activate items, or use actions that have the attack or manipulate trait, except those granted by this spell. You also gain the following effects based on your form.

- **Air** You gain a fly Speed of 20 feet and become [[Invisible]] while you are in the air. You can create the effects of a [[Gust of Wind]] from your space as a 2-action activity, which has the manipulate trait.
- **Mist** You gain a fly Speed of 20 feet, and it becomes hard to see through you. Any creature on one side of your space who is targeted by a creature on the opposite side is [[Concealed]] to the targeting creature.
- **Water** You gain a swim Speed of 20 feet and become invisible while you are in the water. You can electrically charge yourself by taking a single action, which has the manipulate trait. If you do, you are no longer invisible in the water due to electricity indicating your location, but any creature that makes a melee attack against you takes @Damage[(1d6+max(0,floor(@item.rank/2) -3))[electricity]] damage.

> [!danger] Effect: Spell Effect: Tempest Form

**Heightened (+2)** Increase the resistance by 5 and the electricity damage from the charged water form by 1.

**Source:** `= this.source` (`= this.source-type`)
