---
type: action
source-type: "Remaster"
traits: ["[[Champion]]", "[[Divine]]", "[[Emotion]]", "[[Mental]]"]
cast: "`pf2:r`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** An enemy in your champion's aura damages you

**Effect** You put an impertinent foe who dared harm you in their proper place. You command your enemy to kneel before you in obedience. If they dare to refuse, they must pay the price in pain and anguish. The enemy must choose one of the following options.

- **Kneel** The enemy drops [[Prone]] as a free action.
- **Refuse** You deal @Damage[(ternary(gte(@actor.level,19),6,ternary(gte(@actor.level,16),5,ternary(gte(@actor.level,12),4,ternary(gte(@actor.level,9),3,ternary(gte(@actor.level,5),2,1))))))d6[mental]] damage to the enemy. This damage increases to 2d6 at 5th level, 3d6 at 9th level, 4d6 at 12th level, 5d6 at 16th level, and 6d6 at 19th level.

Regardless of which option the enemy chose, your Strikes against it deal 1 extra spirit damage until the end of your next turn. This extra damage increases to 2 at 9th level and 3 at 16th level.

> [!danger] Effect: Champion's Extra Damage

**Source:** `= this.source` (`= this.source-type`)
