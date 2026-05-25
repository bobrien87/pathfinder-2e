---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Godling|Godling]]"
source-type: "Remaster"
level: "12"
traits: ["[[Destiny]]", "[[Mythic]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your Calling allows you to begin walking the path to true deific ascension, inspiring followers as your divine seed grows. Your first follower is your hierophant—the high priest of your new faith—whom you rely on to spread your word and provide an anchoring mortal presence as your perspectives are increasingly pulled toward the cosmic. When you gain this feat, choose one willing ally to be your hierophant. If your hierophant is not trained in spell attack modifier and spell DC, they become trained for as long as they are your designated hierophant. If your hierophant dies or chooses to part ways with you, you can designate a new hierophant by communing with the chosen ally for a period of 24 hours.

Your Calling allows you to seize the divine magic typically restricted to deities. Choose one domain to claim from the list on Player Core, or from other domains you have access to. You learn the initial domain spell for this domain. You gain a pool of Focus Points with 1 Focus Point and you can Refocus by taking 10 minutes to replenish your divine energy from the planes beyond. You gain expert proficiency in spell modifier and spell DC, and your spellcasting ability for these spells is your choice of Wisdom or Charisma, decided when you gain this feat.

Your hierophant also gains the Cast a Spell activity and can cast the domain spell you learned with Godling Dedication. When they Cast the Spell in this way, your Focus Point is expended as the cost of the spell. Your hierophant uses their own spellcasting proficiency in spell modifier and spell DC when casting a spell in this way, and they use their own Wisdom or Charisma modifier (matching your choice). If your hierophant has mythic power, they can spend a Mythic Point to cast any divine spell they gain by being your hierophant at mythic proficiency.

Godling

**Source:** `= this.source` (`= this.source-type`)
