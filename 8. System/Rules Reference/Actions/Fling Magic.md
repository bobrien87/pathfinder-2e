---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Magical]]", "[[Manipulate]]", "[[Thaumaturge]]"]
cast: "`pf2:2`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You are holding your wand implement.

You fling magical energy at a target within 60 feet, dealing @Damage[(ceil(@actor.level/2)+2)d4[untyped]] damage, with a [[Reflex]] save against your class DC. The damage is of the type you selected when you gained your wand implement. At 3rd level and every 2 levels thereafter, the damage increases by 1d4.

You can expend more energy than usual to boost the effect of Fling Magic, dealing @Damage[(ceil(@actor.level/2)+2)d6[untyped]]{d6s of damage} instead of d4s. After you do, the wand's extra energy is discharged; you can't boost the wand's damage again, but can continue to Fling Magic normally. The extra energy recharges at the end of your next turn.

**Special** This activity has the trait corresponding to the damage type you selected.

**Source:** `= this.source` (`= this.source-type`)
