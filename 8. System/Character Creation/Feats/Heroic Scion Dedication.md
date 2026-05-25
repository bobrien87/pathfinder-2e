---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Heroic Scion|Heroic Scion]]"
source-type: "Remaster"
level: "12"
traits: ["[[Destiny]]", "[[Mythic]]"]
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Destiny calls, and the soul of a dead hero reincarnates to take up the fight! Either an old enemy resumes their efforts to affect chaos and violence, or a new threat arises and you feel compelled to stand against it. You've stood against evil before, and the time is nigh for you to do so once again.

When you select this mythic destiny, work with your GM to determine the best choice for which previous PC or NPC serves as the source of your reincarnation. For the Revenge of the Runelords Adventure Path in particular, any PC who played a role in the Rise of the Runelords, Shattered Star, or Return of the Runelords Adventure Paths makes for a perfect fit—as would any allied NPC who, in your previous campaign, perished before the end.

A heroic scion comes into the world when a nemesis from their old adventures returns. In the case of this campaign, the heroic scion's nemesis are the ancient runelords of Thassilon. In other campaigns, this nemesis can be a specific individual, a coterie of rivals, or an organization you're destined to oppose. You instinctively know when your nemesis is active in the world. This knowledge may begin as nightmares or a feeling of inevitable conflict but grows stronger and more specific as you contemplate further. You also know when this entity or group has been fully defeated and ceases to operate at all. You gain a +2 circumstance bonus to Perception checks to [[Seek]] or [[Sense Motive]] whenever an ally or servant of your nemesis attempts to Lie to you, escape your notice, or Impersonate someone else.

Fate has deemed you incredibly hard to kill. You reduce the DC of recovery checks by 1.

Choose one skill that's not a Lore skill, based on the themes of your reincarnated heroic source. Your GM can help you determine a list of appropriate skills to choose from. When you employ an action using that skill, you may spend a Mythic Point to attempt the associated check at mythic proficiency.

Finally, you gain the [[Additional Lore]] feat for a special Lore skill subcategory—Incarnation Lore. This Lore skill allows you to become aware of or recall your past exploits. When you increase your proficiency in Incarnation Lore, you remember more about your previous adventures. Certain heroic scion feats require you to attempt an Incarnation Lore check, such as when you attempt the [[Flash of Memory]] activity granted you by this feat.

Heroic Scion (Rare)

**Source:** `= this.source` (`= this.source-type`)
