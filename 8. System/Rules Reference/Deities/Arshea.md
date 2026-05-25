---
type: deity
source-type: "Remaster"
domains: "Confidence, Freedom, Passion, Perfection"
favored-weapon: "Flail"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Jump]], Rank 2: [[Humanoid Form]], Rank 5: [[Dreaming Potential]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Appearing in art more than any of the other empyreal lords, the Spirit of Abandon represents freedom, physical beauty, and sexuality. More than anything else, freedom is what matters to Arshea. For many this is most commonly seen as freedom for sexual expression, but Arshea represents the freedom to experience all that is good in the world, be it an ideology or a specific emotional or physical expression. So long as it doesn't harm others, Arshea believes creatures should do, think, and feel as they will. They encourage their followers to try new things, to think in new ways, and to wear new forms.

**Areas of Concern** freedom, physical beauty, sexuality

**Title** Spirit of Abandon

**Areas of Concern** Freedom, physical beauty, sexuality

**Edicts** Inspire passion, comfort and free the repressed, seek your true self and desires

**Anathema** Judge another based on sexual desires or gender roles, act without consent in pursuit of passion

**Religious Symbol** figure with colorful sashes

**Sacred Animal** swan

**Sacred Colors** purple, white

**Source:** `= this.source` (`= this.source-type`)
