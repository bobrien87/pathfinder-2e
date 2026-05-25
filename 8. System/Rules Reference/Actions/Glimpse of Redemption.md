---
type: action
source-type: "Remaster"
traits: ["[[Champion]]", "[[Divine]]"]
cast: "`pf2:r`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** An enemy damages your ally, and both are in your champion's aura;

**Effect** Your enemy hesitates under the weight of sin as visions of redemption play in their mind's eye. The enemy must choose to repent or refuse, with the following effects. If the enemy is mindless or otherwise unable to repent, use the refuse result.

- **Repent** The ally is unharmed by the triggering damage.
- **Refuse** The ally gains resistance to all damage against the triggering damage equal to 2 + your level. After the damaging effect is applied, the enemy becomes [[Enfeebled]] 2 until the end of its next turn

> [!danger] Effect: Champion's Resistance

**Source:** `= this.source` (`= this.source-type`)
