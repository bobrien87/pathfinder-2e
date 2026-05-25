---
type: action
source-type: "Remaster"
traits: ["[[Manipulate]]"]
cast: "`pf2:2`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're wearing or holding a [[Healer's Toolkit]].

You perform first aid on an adjacent creature that is [[Dying]] or [[Bleeding]]. If a creature is both dying and bleeding, choose which ailment you're trying to treat before you roll. You can Administer First Aid again to attempt to remedy the other effect.

- **Stabilize** Attempt a Medicine check on a creature that has 0 Hit Points and the dying condition. The DC is equal to 5 + that creature's recovery roll DC (typically 15 + its dying value).
- **Stop Bleeding** Attempt a Medicine check on a creature that is taking persistent bleed damage. The DC is usually the DC of the effect that caused the bleed.
- **Success** If you're trying to stabilize, the target loses the dying condition (but remains [[Unconscious]]). If you're trying to stop bleeding, the target benefits from an assisted recovery with the lowered DC for particularly appropriate help.
- **Critical Failure** If you were trying to stabilize, the target's dying value increases by 1. If you were trying to stop bleeding, the target immediately takes an amount of damage equal to its persistent bleed damage.

**Source:** `= this.source` (`= this.source-type`)
