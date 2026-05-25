---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Magical]]", "[[Thaumaturge]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're holding an implement.

Your implement supercharges your weapon to shoot an impossible volley or carve through your foes. Make a Strike with your weapon against each enemy within 30 feet of you. You don't increase your multiple attack penalty until after making all the attacks. If your weapon is a melee weapon and any of the attacks are outside your reach, you Release the weapon before the Strikes, and it returns to your grasp after all of them. If your hands are full when the weapon returns, it falls to the ground in your space.

**Source:** `= this.source` (`= this.source-type`)
