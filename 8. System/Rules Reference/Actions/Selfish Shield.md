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

**Trigger** An enemy in your champion's aura damages you

**Effect** Your self-interest keeps you safe. You gain resistance against the triggering damage equal to 2 + half your level, regardless of damage type.

> [!danger] Effect: Selfish Shield

In addition, your Strikes against the triggering creature deal 1 extra spirit damage until the end of your next turn. This extra damage increases to 2 at 9th level and 3 at 16th level.

> [!danger] Effect: Champion's Extra Damage

**Source:** `= this.source` (`= this.source-type`)
