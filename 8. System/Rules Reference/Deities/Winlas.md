---
type: deity
source-type: "Remaster"
domains: "Glyph, Knowledge, Protection, Vigil"
favored-weapon: "Mace"
divine-font: "Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Share Lore]], Rank 3: [[Veil Of Privacy]], Rank 4: [[Infectious Melody]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Elder of Divinity

**Areas of Concern** Ceremonies, religiousness, service

**Edicts** Serve leaders of ceremonies, craft ceremonial arms and armor, lead a congregation

**Anathema** Deride sacred ceremonies, carelessly or lazily perform rituals, destroy ceremonial objects

**Religious Symbol** censer and mace

**Sacred Animal** egret

**Sacred Colors** green, silver

**Source:** `= this.source` (`= this.source-type`)
