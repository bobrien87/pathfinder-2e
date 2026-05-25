---
type: action
source-type: "Remaster"
traits: ["[[Champion]]"]
cast: "`pf2:r`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** An enemy damages, [[Grab|grabs]], or [[restrains]] your ally, and both are in your champion's aura

You free an ally from restraint.

If the trigger was an ally taking damage, the ally gains resistance to all damage against the triggering damage equal to 2 + your level.

The ally can attempt to break free of effects grabbing, [[Restraining]], [[Immobilizing]], or [[Paralyzing]] them. They either attempt a new save against one such effect that allows a save, or attempt to [[Escape]] from one effect as a free action.

If they can move, the ally can Step as a free action, even if they didn't need to escape.

> [!danger] Effect: Champion's Resistance

**Source:** `= this.source` (`= this.source-type`)
