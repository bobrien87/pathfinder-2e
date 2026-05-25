---
type: deity
source-type: "Remaster"
domains: "Ambition, Creation, Toil, Wealth"
favored-weapon: "Spear"
divine-font: "Harm"
divine-skill: "Thievery"
divine-spells: "Rank 1: [[Shattering Gem]], Rank 4: [[Creation]], Rank 7: [[Planar Palace]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Mammon, the Grasping One, oversees the vast treasuries of Hell secured in the vaults of Erebus, Hell's third layer. As his angelic form was slain, he has no form of his own, so instead he infuses the very wealth that he guards, taking forms composed of riches and extending his senses out through each nigh-uncountable coin—he knows well the exact sum held in Hell's vaults and the greatest treasures among them. His worshippers are the greedy rich and poor alike, and he often arranges for such mortals to stumble across a "lucky copper" through which he whispers encouragements for the bearer to indulge in greater and greater vices, eventually claiming their soul as his own.

**Title** The Argent Prince

**Areas of Concern** Avarice, watchfulness, wealth

**Edicts** Gain financial control over others, gather new wealth, count your riches

**Anathema** Leave the cult of Mammon, allow those who steal from you to go unpunished

**Religious Symbol** devil-faced coin

**Sacred Animal** rat

**Sacred Colors** gold, silver

**Source:** `= this.source` (`= this.source-type`)
