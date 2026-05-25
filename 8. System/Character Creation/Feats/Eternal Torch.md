---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Fire]]", "[[Impulse]]", "[[Kineticist]]", "[[Light]]", "[[Manipulate]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You open a connection to your kinetic gate, large enough for a torch flame to flow. You create a magical, torch-like flame within 120 feet in any color you choose. It's as bright and hot as a torch. You can have it orbit a target willing creature or emit from a target object that's unattended or attended by a willing creature. If you create a flame on a weapon, you still need to use it as an improvised weapon to attack with the flame, just as with a torch.

The flame has an unlimited duration. You can have a maximum number of Eternal Torches equal to your Constitution modifier, and you can Dismiss each torch individually.

> [!danger] Effect: Eternal Torch

**Level (8th)** All your torches—even ones you already created—shed bright light in a 60-foot radius (and dim light for the next 60 feet).

**Source:** `= this.source` (`= this.source-type`)
