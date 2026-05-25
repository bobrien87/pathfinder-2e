---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Divine]]", "[[Mental]]"]
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You enter a self-imposed trance that helps you push the physical limits of your body. You gain a number of temporary Hit Points equal to your level plus your Constitution modifier. The trance lasts for 1 minute, until you fall [[Unconscious]], or until you Dismiss it, whichever comes first.

While in this trance, you gain a +1 status bonus to Fortitude and Will saving throws and your melee Strikes deal 1 additional spirit damage. Other abilities may require you to be in a spirit trance. When the trance ends, you lose any remaining temporary Hit Points from Enter Spirit Trance, and you can't Enter a Spirit Trance for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
