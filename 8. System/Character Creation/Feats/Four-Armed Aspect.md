---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Morph]]", "[[Primal]]", "[[Yaksha]]"]
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You intone vows to shoulder others' pains; in response, your torso sprouts an additional pair of arms to help you bear those burdens. For the following minute, you can carry 3 more Bulk than normal before becoming encumbered and up to a maximum of 6 more Bulk. You can also use these arms as free hands to perform only the following actions or activities: [[Disarm]], [[Grapple]], [[Shove]], and [[Trip]]. After this minute or when you become [[Unconscious]], whichever comes first, these additional arms fade away.

**Source:** `= this.source` (`= this.source-type`)
