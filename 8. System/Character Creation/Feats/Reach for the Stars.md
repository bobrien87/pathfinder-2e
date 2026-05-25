---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Gunslinger]]"]
prerequisites: "Black Powder Boost"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The sky's the limit, as long as you've got enough black powder. When you use [[Black Powder Boost]], you can expend additional black powder or ammunition to boost yourself farther. For each dose of black powder or piece of firearm ammunition you spend in addition to your shot, you add another 10 feet to the height or distance of your [[Leap]], to a maximum of 5 boosts (a +50-foot status bonus). You must be wearing a dose of black powder or piece of ammunition, or have it in hand, to detonate it for a boost.

You can choose at which points in your Leap you detonate each boost, allowing you to change direction each time. You must then move in a straight line until you boost again or end your Leap.

**Source:** `= this.source` (`= this.source-type`)
