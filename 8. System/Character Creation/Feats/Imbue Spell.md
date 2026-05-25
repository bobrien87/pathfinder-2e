---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wildspell|Wildspell]]"
source-type: "Remaster"
level: "16"
traits: ["[[Concentrate]]", "[[Mythic]]"]
prerequisites: "Wildspell Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** Your previous action was to Cast a Spell.

You pass the energy of your magic onto an ally, allowing another to release the spell. Upon completing the Casting of a Spell, instead of the normal effects of the spell, you imbue the energy of that spell to an ally that's adjacent to you or within your [[Spellsurge]] aura. You expend the spell, spell slot, or Focus Point as normal. At any time during the next hour, that ally can release the energy of the spell with a single action that has the concentrate and manipulate traits; they don't need to expend any spell slots or Focus Points. All attributes of the spell are determined based on your original casting of the spell, including any spellshape feats used, but the ally is treated as the spellcaster for determining the origin of the spell and for making any choices the spell requires. If the spell must or can be Sustained, your ally takes the action to Sustain it. You can't target yourself with this ability. If the spell isn't released by the ally within 1 hour, the energy dissipates. You can only have one spell imbued at a time; additional uses of this ability cause previously imbued spells to dissipate immediately

**Source:** `= this.source` (`= this.source-type`)
