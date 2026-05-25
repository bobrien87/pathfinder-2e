---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Nephilim]]"]
prerequisites: "Proteankin"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The magic in your blood is unpredictable. When you make your daily preparations, roll `r 1d12` twice and consult the following list:

1

[[Acid Grip]]

2

[[Blur]]

3

[[Gecko Grip]]

4

[[Humanoid Form]]

5

[[Illusory Object]]

6

[[Laughing Fit]]

7

[[Noise Blast]]

8

[[Resist Energy]]

9

[[See the Unseen]]

10

[[Shatter]]

11

[[Shrink]]

12

[[Telekinetic Maneuver]]

You can cast each of those two spells once during the following day (or one spell twice if you rolled the same number) as 2nd-rank divine innate spells

**Source:** `= this.source` (`= this.source-type`)
