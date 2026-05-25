---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beastmaster|Beastmaster]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Nature"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You gain the service of a young animal companion that travels with you and obeys your commands. Contrary to the usual rules for animal companions, this feat can grant you a second animal companion. If you ever have more than one animal companion, you gain the Call Companion action. See the Beastmaster Animal Companions sidebar for details on this action.

Certain beastmaster feats give you focus spells. When you gain your first beastmaster focus spell, you become trained in the spell attack modifier and spell DC statistics. Your key spellcasting attribute for beastmaster archetype spells is Charisma, and they are primal spells. You can Refocus by feeding, playing with, or otherwise tending to an animal companion.

**BEASTMASTER ANIMAL COMPANIONS**

If you're playing a beastmaster, you determine the statistics and abilities of your animal companions. As a beastmaster, it's possible for you to have more than one animal companion at one time—up to four companions—but only one of those companions, your "active companion," follows you during exploration and in encounters; the rest are nearby, usually foraging or hunting for food. As soon as you gain a second animal companion from the Beastmaster archetype, you also gain [[Call Companion]] to switch your active companion. These rules apply to all your companions, regardless of whether you got the animal companion from the beastmaster archetype or from another source.

Beastmaster

**Source:** `= this.source` (`= this.source-type`)
