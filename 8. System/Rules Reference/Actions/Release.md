---
type: action
source-type: "Remaster"
traits: ["[[Manipulate]]"]
cast: "`pf2:0`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You release something you're holding in your hand or hands. This might mean dropping an item, removing one hand from your weapon while continuing to hold it in another hand, releasing a rope suspending a chandelier, or performing a similar action. Unlike most manipulate actions, Release does not trigger reactions that can be triggered by actions with the manipulate trait (such as Reactive Strike).

If you want to prepare to Release something outside of your turn, use the [[Ready]] activity.

**Source:** `= this.source` (`= this.source-type`)
