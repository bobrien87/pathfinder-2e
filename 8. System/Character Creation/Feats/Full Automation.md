---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Inventor]]"]
prerequisites: "armor, construct, or weapon innovation"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You become so entwined with your innovations that you can use them without a second thought. You're permanently [[Quickened]]. How you can use the extra action depends on your innovation.

- **Armor** Your armor responds to the most subtle stimuli to move you in the right direction as long as you are wearing it. You can use the extra action to Stride, Step, or use a form of movement provided by your innovation (such as Fly or Swim).

- **Construct** Your ability to command your construct becomes instinctive. You can use the extra action to Command your construct innovation (or to provide 1 of the actions if you choose to spend 2 actions to Command your construct).

- **Weapon** Your weapon becomes easier to wield with deadly efficacy, almost as if it is an extension of your body. It speeds effortlessly toward whatever target you choose as long as you are holding it. You can use the extra action to Strike with your innovation.

**Source:** `= this.source` (`= this.source-type`)
