---
type: deity
source-type: "Remaster"
domains: "Knowledge, Protection, Star, Truth"
favored-weapon: "Starknife"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Gentle Landing]], Rank 4: [[Containment]], Rank 5: [[Mind Probe]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Feather of Truth

**Areas of Concern** Justice, law, order, truth

**Edicts** Defend civilization from chaos, live an honest and just life, be impartial in judgment and reveal the truth

**Anathema** Deal unfairly with your family or community, destroy the environment, lie

**Religious Symbol** blue ostrich feather

**Sacred Animal** leopard

**Sacred Colors** blue, red

**Source:** `= this.source` (`= this.source-type`)
