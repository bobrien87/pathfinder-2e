---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Godling|Godling]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Godling Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your dominion over the divine truths of the world increases. You can lay claim to up to three additional domains, to a total maximum of four. Your mortal form cannot easily contain such power, however—each day during your daily preparations, decide which of your domains you are currently drawing power from; you gain access to this domain for the day and can cast its domain spells as normal, while your ability to access the power of your other domains lies dormant. You learn the advanced domain spell for any domain that you have claimed with your godling abilities.

When you gain this feat, you can choose not to lay claim to one or more domains immediately, instead leaving the space open until later in your story. As long as you have one or more domains unclaimed, you can spend a Mythic Point as a single action to claim a domain, even in the heat of battle, immediately making this your active domain. This domain remains a part of your portfolio forever and cannot be changed after this point.

You can also spend a Mythic Point to overcharge your divine power, gaining access to all the domains you have claimed for the next minute and passing this access on to your hierophant as normal. After the minute ends, you can choose which of the four domains you retain access to until your next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
