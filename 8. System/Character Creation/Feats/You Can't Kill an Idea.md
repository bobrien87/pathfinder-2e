---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Mythic]]"]
prerequisites: "Broken Chain Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Those who would destroy you instead transform you into a powerful yet formless entity. If you would be killed while you have an [[Ultimatum of Liberation]] active, you (along with your equipment) become an ideaform.

As an ideaform, you are [[Invisible]] and incorporeal. You have only 1 Hit Point and can't gain more, but you are immune to all damage; if your [[Dying]] or [[Doomed]] condition would increase to a high enough value to kill you, it does not increase, and you are immune to any effect that would instantly kill or destroy you. You are immune to the [[Unconscious]] condition, yet can take only purely mental actions. You can communicate telepathically with your allies at unlimited range, and gain two extra reactions at the start of each of your turns.

Additionally, you can Aid allies through nothing but telepathic advice, without having to spend an action to prepare first, and can spend a Mythic Point to do so at mythic proficiency. Any circumstance bonus you grant through Aiding is increased by 1.

> [!danger] Effect: You Can't Kill an Idea

Before an hour passes while being an ideaform, you must choose a willing follower of your cause to fuse with and cease to be an ideaform. Use your level, their ancestry, heritage, and ancestry feats, and work with your GM to choose which combination of class, attribute modifiers, skills, and feats would make a good representation of this fusion. This new character has all your previous equipment. If you do not fuse with a follower after an hour of being an ideaform, you cease to be an ideaform and die; the equipment you had at the time of your original death also ceases to exist.

**Source:** `= this.source` (`= this.source-type`)
