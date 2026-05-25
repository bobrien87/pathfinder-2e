---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Draconic Acolyte|Draconic Acolyte]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Arcana, Nature, Occultism, or Religion"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

As an acolyte of dragonkind, you have an item known as a draconic gift that you can use to summon a portion of the magical essence of the dragon you received it from. Choose a Draconic Benefactor with a trait that matches the trained skill you used to qualify for this feat (arcane for Arcana, primal for Nature, occult for Occultism, and divine for Religion). You can't change your draconic benefactor later. You gain the [[Additional Lore]] feat for Dragon Lore. If you were already trained in Dragon Lore, you also become trained in a Lore skill of your choice.

You gain a *draconic gift*, a palm-sized magic item of negligible Bulk with a level equal to your level and a trait matching your draconic benefactor's tradition. Choose this item's appearance when you take this feat. This item is linked to your spirit, so if you ever lose possession of it (whether by dropping it or having it stolen from your person), it appears back in your possession at the beginning of your next turn.

Finally, you gain the [[Channel Draconic Essence]] action and [[Draconic Salvation]] reaction. These and all other actions from this archetype gain the tradition trait of your draconic benefactor.

**Source:** `= this.source` (`= this.source-type`)
