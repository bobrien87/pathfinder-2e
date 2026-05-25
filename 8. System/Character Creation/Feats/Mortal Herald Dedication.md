---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mortal Herald|Mortal Herald]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "worshipper of a specific deity, master in Religion or your deity's divine skill"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You become a mortal herald of your deity, gaining power in return for your service. Others intuitively sense your connection with your deity, which subtly influences the way they act around you. You become bound by your deity's anathema. Depending on your deity, their sanctification can make you holy or unholy. This gives you the holy or unholy trait, which commits you to one side of a struggle over the souls of the planes and can be referenced in other abilities. If you "can be" holy or unholy according to your deity, you make that choice, and if you "must be" holy or unholy you gain the trait automatically. If you gain the opposing trait in some way, you lose the previous trait until you complete an [[Atone]] ritual.

In addition, once per day, you can cast [[Heal]] as a 6th-rank innate divine spell. You can only target yourself with the spell, but you gain the benefits of the 2-action version when you spend 1 action to cast it. In addition, if you would be reduced to 0 Hit Points but not immediately killed, you can cast the spell as a free action before you become [[Unconscious]]. This spell is automatically heightened to a rank equal to half your level.

**Special** If you have void healing, you instead cast [[Harm]].

Mortal Herald

**Source:** `= this.source` (`= this.source-type`)
