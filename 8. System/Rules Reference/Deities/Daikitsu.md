---
type: deity
source-type: "Remaster"
domains: "Change, Creation, Family, Nature"
favored-weapon: "Flail"
divine-font: "Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Pest Form]], Rank 2: [[Humanoid Form]], Rank 5: [[Illusory Scene]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

It is not surprising that the Tian Xia goddess Daikitsu is a common object of veneration, given that she has the everyday subjects of rice, agriculture, and craftsmanship under her divine purview. Her holy symbol is that of a nine-tailed fox.

**Title** Lady of Foxes

**Areas of Concern** Agriculture, craftsmanship, kitsune, rice

**Edicts** Ensure the health of crops and vegetation, perfect a craft or trade, leave offerings for foxes, celebrate the turning of the seasons

**Anathema** Mistreat your tools, pass a beggar without giving alms, discriminate against sex workers or the lower class, commit murder or torture, harm an innocent

**Religious Symbol** nine-tailed fox

**Sacred Animal** fox

**Sacred Colors** red, white

**Source:** `= this.source` (`= this.source-type`)
