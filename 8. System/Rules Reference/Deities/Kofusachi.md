---
type: deity
source-type: "Remaster"
domains: "Luck, Passion, Travel, Wealth"
favored-weapon: "Staff"
divine-font: "Heal"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Soothe]], Rank 2: [[Laughing Fit]], Rank 8: [[Uncontrollable Dance]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Laughing God

**Areas of Concern** Abundance, discovery, happiness, prosperity

**Edicts** Support local businesses, bring prosperity to your community, sample life's pleasures

**Anathema** Become tied to one location, judge another based on sexual desires or gender roles, harm innocents, spread despair, commit murder

**Religious Symbol** string of seven coins

**Sacred Animal** dog

**Sacred Colors** gold, orange

**Source:** `= this.source` (`= this.source-type`)
