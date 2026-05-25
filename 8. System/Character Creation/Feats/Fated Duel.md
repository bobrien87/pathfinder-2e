---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Prophesied Monarch|Prophesied Monarch]]"
source-type: "Remaster"
level: "18"
traits: ["[[Mythic]]"]
prerequisites: "Prophesied Monarch Dedication"
frequency: "once per P1W"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per week

You and your knights are an unbeatable force together, but sometimes it's a monarch's duty to resolve the fate of their kingdom with nothing more than their own trusted weapon. Spend a Mythic Point, and choose one opponent within 30 feet; you declare a Fated Duel against that opponent.

If the opponent accepts your challenge, you're locked in mystical combat together. Neither you nor your opponent can move more than 30 feet from each other; you both can't be harmed by any creature other than each other; and you both can't harm any creature other than each other. This mystical bond is incredibly draining on both parties, pulling at their life and spirit; if neither you nor your opponent has defeated the other by the time 1 minute has passed, you both become [[Doomed]] 1. Your doomed conditions increase by 1 for each additional minute that passes until one or both of you die.

If your opponent refuses your challenge, you regain a Mythic Point and can immediately attempt an Intimidation check at mythic proficiency to [[Demoralize]] them.

**Source:** `= this.source` (`= this.source-type`)
