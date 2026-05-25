---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Inventor]]", "[[Manipulate]]", "[[Unstable]]"]
prerequisites: "armor, construct, or weapon innovation"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** Your turn begins.

You can use unstable clockwork devices in your innovation to push your invention to act more quickly. You are [[Quickened]] for this turn. How you can use the extra action depends on your innovation.

- **Armor** You can use the extra action to Step, Stride, or use another movement action granted by your innovation (such as Swim if you have the Diving Armor feat).
- **Construct** You can use the extra action to Command your construct innovation (or to provide 1 of the actions if you spend 2 actions to Command your construct).
- **Weapon** You can use the extra action to Strike with your innovation or Reload your innovation.

**Source:** `= this.source` (`= this.source-type`)
