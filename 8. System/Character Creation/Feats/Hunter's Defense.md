---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Tripkee]]"]
prerequisites: "trained in Nature"
frequency: "once per PT1H"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Trigger** A creature with the animal, beast, elemental, fey, fungus, or plant trait attacks you, and you can see the attacker.

Your canny understanding of natural and primal creatures helps you predict and dodge their attacks. The triggering attack roll targets your Nature DC instead of your AC. Though this allows you to avoid taking penalties to your AC, it doesn't remove any conditions or other effects causing such penalties. For example, an enemy with sneak attack would still deal extra damage to you for being [[Off Guard]], even though you wouldn't take the –2 circumstance penalty against the attack.

**Source:** `= this.source` (`= this.source-type`)
