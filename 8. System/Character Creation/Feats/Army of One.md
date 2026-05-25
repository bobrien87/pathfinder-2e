---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ascended Celestial|Ascended Celestial]]"
source-type: "Remaster"
level: "18"
traits: ["[[Concentrate]]", "[[Flourish]]", "[[Mythic]]"]
prerequisites: "Ascended Celestial Dedication, Celestial Armaments"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your nimbus is active.

Even alone, you're a force to be reckoned with—an army of one, so long as you have your celestial armaments. Spend 1 Mythic Point. If you're not currently wielding your celestial armament, it immediately teleports into your hand. With a gesture and a whispered prayer, you launch your celestial armament into the air, where it flies with a mind of its own, attacking every enemy within your nimbus. Make a Strike with that weapon against each enemy in the bright light of your nimbus. Each attack counts toward your multiple attack penalty, but your penalty doesn't increase until you have made all your attacks. After these attacks are complete, your weapon returns to your hand.

**Source:** `= this.source` (`= this.source-type`)
