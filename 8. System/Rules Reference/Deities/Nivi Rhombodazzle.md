---
type: deity
source-type: "Remaster"
domains: "Family, Luck, Trickery, Wealth"
favored-weapon: "Light-hammer"
divine-font: "Harm, Heal"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Illusory Disguise]], Rank 2: [[Invisibility]], Rank 4: [[Liminal Doorway]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Goddess of gems, stealth, and gambling, Nivi Rhombodazzle is the ultimate high roller, said to have won her divinity from the dwarven god Torag in exchange for a particular gemstone. Nivi's love of gambling was born not from the rush of victory, but from the excitement of the bet itself, an attitude that ultimately brought her into a situation where her debts outweighed her charms. Keeping one step ahead of her creditors, Nivi fled beneath the earth and into the Darklands. Most of her adventures in the lightless lands are lost to time and history, but she ultimately emerged reborn as a goddess, hailed as the first of the deep gnomes—uncanny underground gnomes with unique magical abilities and immunity to the dread Bleaching, a wasting curse which claims the lives of gnomes who succumb to boredom and ennui.

**Title** The Gray Polychrome

**Areas of Concern** gambling, gems, gnomes, and stealth

**Edicts** learn the rules and strategies of games of chance played wherever you travel, take risks and savor the consequences whether good or ill, use stealth and guile over violence when dealing with the fallout from your risk-taking

**Anathema** break the established rules or terms of a wager, use violence to avoid the consequences of a wager

**Religious Symbol** seven-pipped gem die

**Sacred Animal** mole

**Sacred Colors** gray, red

**Source:** `= this.source` (`= this.source-type`)
