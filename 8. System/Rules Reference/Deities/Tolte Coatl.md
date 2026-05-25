---
type: deity
source-type: "Remaster"
domains: "Creation, Glyph, Knowledge, Travel"
favored-weapon: "Arbalest"
divine-font: "Heal"
divine-skill: "Society"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Tolte Coatl (TOLL-teh coh-AHtl) is the youngest of the tribunal, but sometimes seen as the leader of three. While he is always looking to help mortals and share righteous ideals with them, Tolte Coatl is more concerned with matters of the mind than the more physical pursuits of his siblings. He teaches that knowledge isn't simply accumulated all at once, it's slowly built up, like a home being built one brick at a time; knowledge must generally be built upon itself. One can't know how to cook for oneself until they know how to create a fire. Tolte Coatl encourages patience with learning and acquiring new skills. He also encourages sharing knowledge when it can help others. As such, he sometimes grants his followers gifts of small pieces of vital information that can help unlock new collections of knowledge, such as a vital component to a new invention or a portion of an alchemical formula.

**Title** The Crafter of Knowledge

**Areas of Concern** Knowledge, memories, migration

**Edicts** Encourage others to join you on travels, offer to teach those who are genuinely eager to learn, ask others to share their tales

**Anathema** Alter the memory of another, deny someone who genuinely wishes to journey with you and would not harm you

**Religious Symbol** wing raining down stars

**Sacred Animal** moth

**Sacred Colors** green, blue

**Source:** `= this.source` (`= this.source-type`)
