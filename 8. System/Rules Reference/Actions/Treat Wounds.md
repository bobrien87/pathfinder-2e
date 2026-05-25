---
type: action
source-type: "Remaster"
traits: ["[[Exploration]]", "[[Healing]]", "[[Manipulate]]"]
cast: "Passive"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're wearing or holding a [[Healer's Toolkit]].

You spend 10 minutes treating one injured living creature (targeting yourself, if you so choose). The target is then temporarily 

> [!danger] Effect: Immune

 to Treat Wounds actions for 1 hour, but this interval overlaps with the time you spent treating (so a patient can be treated once per hour, not once per 70 minutes).

The Medicine check DC is usually 15, though the GM might adjust it based on the circumstances, such as treating a patient outside in a storm, or treating magically cursed wounds. If you're an expert in Medicine, you can instead attempt a DC 20 check to increase the Hit Points regained by 10; if you're a master of Medicine, you can instead attempt a DC 30 check to increase the Hit Points regained by 30; and if you're legendary, you can instead attempt a DC 40 check to increase the Hit Points regained by 50. The damage dealt on a critical failure remains the same.

If you succeed at your check, you can continue treating the target to grant additional healing. If you treat it for a total of 1 hour, double the Hit Points it regains from Treat Wounds.

The result of your Medicine check determines how many Hit Points the target regains.

[[Treat Wounds]]
- **Critical Success** The target regains `r 4d8[healing] #Treat Wounds` Hit Points and loses the [[Wounded]] condition.
- **Success** The target regains `r 2d8[healing] #Treat Wounds` Hit Points, and loses the wounded condition.
- **Critical Failure** The target takes `r 1d8[damage] #Treat Wounds (Critical Failure)` damage.

**Source:** `= this.source` (`= this.source-type`)
