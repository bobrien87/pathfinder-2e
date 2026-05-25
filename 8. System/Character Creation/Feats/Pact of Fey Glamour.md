---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pactbinder|Pactbinder]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Illusion]]", "[[Primal]]"]
prerequisites: "Pactbinder Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've sworn a pact with fey powers, granting you the otherworldly appearance of your dreams in exchange for oaths of hospitality. As long as you keep your end of the bargain, your base appearance changes indefinitely to any one appearance you wish that's within the bounds of possibility for your ancestry; this effect can't be counteracted or removed except by violating the pact. Additionally, you can cast [[Illusory Disguise]] as a primal innate spell once per hour, using the higher of your class DC and your spell DC to determine the DC.

In exchange, you promise to accept any fey's request for hospitality, granting them food, drink, and lodging for up to 3 days and 3 nights. You also promise not to harm any creature to whom you've offered hospitality or who has shown hospitality to you, whether or not that creature is fey, unless that creature does harm first. If you refuse hospitality to a fey or violate hospitality, you lose the benefits of this feat until you atone for your transgressions, instantly reverting your appearance to the one you had before the pact.

**Source:** `= this.source` (`= this.source-type`)
