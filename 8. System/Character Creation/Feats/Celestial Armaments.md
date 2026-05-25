---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ascended Celestial|Ascended Celestial]]"
source-type: "Remaster"
level: "16"
traits: ["[[Mythic]]"]
prerequisites: "Ascended Celestial Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You imbue a fragment of your divine spark into a weapon, blessing your blade and transforming it into a weapon worthy of the celestial realms. Select one weapon or [[Handwraps of Mighty Blows]] when you make your daily preparations. The weapon sheds light like a torch, deals an additional 1d8 spirit damage, and creatures who wield it gain the weapon's critical specialization.

When you critically hit a target with the weapon, the target must succeed at a [[Fortitude]] save against your class DC or spell DC (whichever is higher) or be [[Blinded]] for 1d4 rounds.

> [!danger] Effect: Celestial Armaments

As a single action that has the concentration trait, you can hold your hand aloft and call this weapon back to your possession; it immediately teleports into your hand.

While you're holding this weapon, you can spend 1 Mythic Point as a single action to temporarily grant a blessing to weapons wielded by your allies. Each ally within the bright light of your nimbus when you take this action selects one weapon in their possession. For 1 minute, the selected weapons gain the following benefits: the weapon sheds light like a torch, the weapon deals an additional 1d6 spirit damage, and creatures who wield the weapon gain the weapon's critical specialization.

> [!danger] Effect: Celestial Armaments (Allies)

**Source:** `= this.source` (`= this.source-type`)
