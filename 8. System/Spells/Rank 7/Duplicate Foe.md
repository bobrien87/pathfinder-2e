---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "30 feet"
targets: "1 enemy of level 15 or lower"
defense: "Fortitude"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a temporary duplicate of an enemy to fight on your behalf. The target can attempt a Fortitude save to disrupt the spell. The duplicate appears in an unoccupied space adjacent to the target and has the target's attack modifier, AC, saving throw modifiers, Perception, and skill modifiers, but it has only 70 Hit Points and lacks the target's special abilities, including immunities, resistances, and weaknesses. It has no magic items except weapon potency runes.

The duplicate gains the minion trait, and it can only Stride and Strike. Its Strikes deal the target's normal damage but don't apply added effects, since it doesn't have special abilities. The spell automatically ends if the duplicate's Hit Points drop to 0.

The duplicate attacks your enemies to the best of its abilities. You can also try to give it additional instructions; when you Sustain the spell, you can also Command a Minion as part of your action, but the GM determines whether the duplicate follows your command.

The duplicate is unstable, so each turn after it takes its actions, it loses 4d6 Hit Points. It's not a living creature, and it can never regain its lost Hit Points in any way.
- **Critical Success** You fail to create a duplicate.
- **Success** The duplicate deals half damage with its Strikes and the duration is reduced to a maximum of 2 rounds.
- **Failure** The duplicate works as described.

**Heightened (+1)** The level of creature you can target increases by 2. The duplicate has 10 more HP.

**Source:** `= this.source` (`= this.source-type`)
