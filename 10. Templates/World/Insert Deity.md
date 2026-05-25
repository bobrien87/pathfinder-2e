---
type: deity
source-type: "{source-type}"
sanctification: "{sanctification}"
alignment: "{alignment}"
portfolio: "{portfolio}"
domains: "{domains}"
favored-weapon: "{favored-weapon}"
divine-font: "{divine-font}"
divine-skill: "{divine-skill}"
divine-spells: "{divine-spells}"
source: "{source}"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

{description}

**Source:** `= this.source` (`= this.source-type`)
