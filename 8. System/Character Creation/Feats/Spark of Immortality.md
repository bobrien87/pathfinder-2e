---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mortal Herald|Mortal Herald]]"
source-type: "Remaster"
level: "20"
traits: ["[[Archetype]]", "[[Mythic]]"]
prerequisites: "Mortal Herald Dedication"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have become a divine entity, no longer entirely mortal. You no longer age, and you die only when you reach dying 5 (dying 6 if you have [[Diehard]]). Upon your death, your body and soul are transported to bask in the presence of your deity. Your god can decide to rebuild your mortal form and return you to the point of your death or some other safe location, or allow you to rest as an honored guest in their realm until you are needed once more. Typically, your god restores you if whatever quest you're undertaking, such as defeating a malevolent tyrant or returning a stolen artifact, remains incomplete.

**Source:** `= this.source` (`= this.source-type`)
