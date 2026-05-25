---
type: deity
source-type: "Remaster"
domains: "Cities, Earth, Travel, Wealth"
favored-weapon: "Crossbow"
divine-font: "Harm, Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Illusory Object]], Rank 4: [[Creation]], Rank 7: [[Planar Palace]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Abadar is worshipped among most as a god of commerce, civilization, and order. He values dispassionate, impartial neutrality, and courts disparate divine allies as a means of learning all perspectives and using all available resources, whether or not he agrees with them. While most of his followers interpret his holy mandates by uplifting their communities and upholding law and order, his doctrine is easily twisted to objectivism and prosperity theology by those who wish to enrich themselves. He is also the Master of the First Vault, a divine trove that holds the perfect version of every type of creature and object.

**Title** Master of the First Vault

**Areas of Concern** cities, law, merchants, wealth

**Edicts** bring civilization to the frontiers, earn wealth through hard work and trade, follow the rule of law

**Anathema** engage in banditry or piracy, steal, undermine a law-abiding court

**Religious Symbol** golden key

**Sacred Animal** monkey

**Sacred Colors** gold, silver

**Source:** `= this.source` (`= this.source-type`)
