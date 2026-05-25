---
type: deity
source-type: "Remaster"
domains: "Healing, Passion, Protection, Travel"
favored-weapon: "Staff"
divine-font: "Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Soothe]], Rank 2: [[False Vitality]], Rank 4: [[Peaceful Bubble]]"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Ever-Lost

**Areas of Concern** Chronic illness, compassion

**Edicts** Cure diseases, offer comfort to the downtrodden, create medicine and curatives

**Anathema** Mock the unwell, knowingly spread disease, knowingly boast of your fortune and health in the presence of someone who is suffering

**Religious Symbol** Aloe plant with radiant halo

**Sacred Animal** Beetle

**Sacred Colors** Green

**Source:** `= this.source` (`= this.source-type`)
