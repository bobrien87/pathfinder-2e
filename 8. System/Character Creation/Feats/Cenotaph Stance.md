---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Lastwall Sentry|Lastwall Sentry]]"
source-type: "Remaster"
level: "20"
traits: ["[[Archetype]]", "[[Stance]]"]
prerequisites: "Lastwall Warden"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a shield.

You take on a stance that marks your location as a place where none will fall. When you enter this stance and at the beginning of each of your turns while in Cenotaph Stance, you gain 10 temporary Hit Points that last until the start of your next turn. If you move or are forced to move, you automatically leave Cenotaph Stance. While in Cenotaph Stance, you're treated as always having the required shield raised. In addition, you can use your [[Shield Block]] reaction when an ally within 15 feet of you takes physical damage, in addition to its normal trigger, thus preventing the ally from taking damage instead of you. Finally, you gain an additional reaction at the start of each of your turns that can be used only for Shield Block.

**Special** If you can use Shield Block to reduce damage that isn't physical damage (for instance, if you have the [[Bless Shield]] or [[Necromantic Bulwark]] feat), you can use your Shield Block reaction when an ally within 15 feet of you takes damage that you could prevent with Shield Block.

**Source:** `= this.source` (`= this.source-type`)
