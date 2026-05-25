---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Razmiran Priest|Razmiran Priest]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Razmiran Priest Dedication, expert in Crafting"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have reached the 12th Step and been instructed in greater secrets of Razmir's doctrine. You can Craft your [[Razmiri Mask]] out of silver or upgrade your existing mask to a silver one in the same time it takes to Craft one made of iron. A Silver Razmiri Mask grants a +2 item bonus to Deception checks to [[Lie]] or [[Feint]], is a 10th-level item, and gains the following activation in addition to that possessed by the standard mask.

**Activate—Call Upon Razmir's Mercy** `pf2:2` (concentrate, manipulate, occult)

**Frequency** three times per day

**Effect** Exhorting Razmir to purge impurities from your target, you lay hands on a creature within reach and cast [[Cleanse Affliction]] as an occult spell with a spell rank equal to half your level. Unlike a normal *cleanse affliction* spell, this doesn't reduce the stage of the affliction; instead, if the counteract check is successful, the affliction's stage is temporarily reduced by 1 and its effects are suppressed for 24 hours, after which the affliction resumes in full force. If the target would have been required to attempt additional saves against the affliction during the 24 hours it was suppressed, they must attempt all of those saving throws as soon as the 24-hour duration ends. This could mean that the target saves successfully and it is as if the affliction were truly healed, or it could mean that the affliction returns and advances multiple stages all at once.

**Source:** `= this.source` (`= this.source-type`)
