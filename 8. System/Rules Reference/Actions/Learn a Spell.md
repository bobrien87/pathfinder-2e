---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Exploration]]"]
cast: "Passive"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Magical Traditions and SkillsEach magical tradition has a corresponding skill, as shown on the table below. You must have the trained proficiency rank in a skill to use it to Identify Magic or Learn a Spell. Something without a specific tradition, such as an item with the magical trait, can be identified using any of these skills.

Magical TraditionCorresponding SkillArcaneArcanaDivineReligionOccultOccultismPrimalNature**Requirements** You have a spellcasting class feature, and the spell you want to learn is on your magical tradition's spell list.

You can gain access to a new spell of your tradition from someone who knows that spell or from magical writing like a spellbook or scroll. If you can cast spells of multiple traditions, you can Learn a Spell of any of those traditions, but you must use the corresponding skill to do so. For example, if you were a cleric with the bard multiclass archetype, you couldn't use Religion to add an occult spell to your bardic spell repertoire.

To learn the spell, you must do the following:

- Spend 1 hour per spell rank, during which you must remain in conversation with a person who knows the spell or have the magical writing in your possession.
- Have materials with the Price indicated in the Learning a Spell table.
- Attempt a skill check for the skill corresponding to your tradition (DC determined by the GM, often close to the DC on the Learning a Spell Table). Uncommon or rare spells have higher DCs; full guidelines for the GM appear on page 52 of GM Core.

Learning a SpellSpell RankPriceTypical DC1st or cantrip2 gp152nd6 gp183rd16 gp204th36 gp235th70 gp266th140 gp287th300 gp318th650 gp349th1,500 gp3610th7,000 gp41**Critical Success** You expend half the materials and learn the spell.
- **Success** You expend the materials and learn the spell.
- **Failure** You fail to learn the spell but can try again after you gain a level. The materials aren't expended.
- **Critical Failure** As failure, except you expend half the materials.

**Source:** `= this.source` (`= this.source-type`)
