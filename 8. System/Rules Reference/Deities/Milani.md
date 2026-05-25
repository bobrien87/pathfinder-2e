---
type: deity
source-type: "Remaster"
domains: "Change, Destruction, Freedom, Zeal"
favored-weapon: "Morningstar"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Sure Strike]], Rank 3: [[Enthrall]], Rank 4: [[Fire Shield]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Milani is the patron mother of those who war against oppression. Once a saint of Aroden's faith, she rewards those willing to sacrifice their lives and use whatever tools are available to fight for those who cannot defend themselves, especially people who have been captured or enslaved. Throughout Golarion, Milani is also known as the Everbloom, as the symbol of her church is a beautiful rose growing from blood-soaked soil.

**Title** The Everbloom

**Areas of Concern** devotion, hope, uprisings

**Edicts** confront oppression in all its forms, defend the common folk, overcome despair to sieve victory

**Anathema** abandon those in need, enslave or oppress others, harm the innocent through direct or inadvertent action

**Religious Symbol** rose on bloody street

**Sacred Animal** mouse

**Sacred Color** red, white

**Source:** `= this.source` (`= this.source-type`)
