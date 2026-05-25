---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Inventor]]"]
prerequisites: "Diving Armor"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** Tian Xia origin

You've rigged your armor innovation with a gizmo that can safely synthesize two sea mines a day, holding them in a protected compartment. You must be submerged in water to use this action, and the mines only detonate if they're underwater.

You off-load a mine onto an unoccupied square within your reach. The mine is primed to explode when a Small or larger creature moves into its square, or when you Interact to Activate your gizmo's remote detonation button, which explodes a single mine up to 50 feet away. As a 1-minute activity, you can hide a mine. Creatures can detect a hidden mine as they would any trap or hazard, using your Craft DC as the Stealth DC. If you don't Conceal the mine, its position is obvious.

Any creature in a @Template[type:emanation|distance:5] around the mine when it detonates takes @Damage[ceil(@actor.level/2)d4[bludgeoning],1d4[piercing]|options:area-damage] damage, with a [[Reflex]] save against your class DC. The bludgeoning damage of your mines increases by 1d4 at 8th level and every 2 levels thereafter. Any mines that haven't detonated when you make your daily preparations become inert and harmless.

**Unstable Function** You push the safety limits of your gizmo, forcing it to synthesize and launch additional sea mines, exceeding the daily limit. Add the unstable trait to Xidao Sea Mine Drop. You create up to 3 additional sea mines that you can immediately deploy in different unoccupied spaces up to 30 feet away.

**Source:** `= this.source` (`= this.source-type`)
