---
type: deity
source-type: "Remaster"
domains: "Cities, Travel, Water, Wealth"
favored-weapon: "Scimitar"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Tailwind]], Rank 3: [[Enthrall]], Rank 5: [[Mariner'S Curse]]"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Merchant Maiden

**Areas of Concern** Commerce, sea travel

**Edicts** Spend time on board a ship at sea, seek new routes between areas, encourage trade and commerce

**Anathema** Sabotage a seagoing vessel, knowingly fleece a customer, watch the sun set while at sea

**Religious Symbol** Bar of gold on waves

**Sacred Animal** Dugong

**Sacred Colors** Gold, teal

**Source:** `= this.source` (`= this.source-type`)
