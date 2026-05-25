---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "expert in Society, Streetwise"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're connected to groups that know what's going on in the streets, and you can get information out of them quickly. When you use Society to [[Gather Information]] in an area where you have a network (typically a settlement where you've spent at least a week or spent a day of downtime to build a network faster), you can contact a member of these groups to get information directly from them. This usually takes about an hour, and it doesn't draw as much attention as Gathering Information in public might. The check and information gained otherwise follow the normal rules for Gather Information.

In addition, if you have successfully consulted the underground network, you get a +1 circumstance bonus to the next check to [[Recall Knowledge]] you attempt about the subject you were Gathering Information on, or a +2 circumstance bonus if you're using Underworld Lore for the check. The GM might change the Lore skill related to the network depending on your location or the specifics of the network you're tapping into.

**Source:** `= this.source` (`= this.source-type`)
