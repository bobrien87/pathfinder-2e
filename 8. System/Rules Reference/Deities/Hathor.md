---
type: deity
source-type: "Remaster"
domains: "Family, Passion, Sun, Wealth"
favored-weapon: "Shortsword"
divine-font: "Heal"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Charm]], Rank 2: [[One With Plants]], Rank 8: [[Uncontrollable Dance]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Hathor is a member of the pantheon often worshiped in Ancient Osirion.

**Title** Mistress of Jubilation

**Areas of Concern** Dance, joy, love, music, the sky

**Edicts** Give wealth to new families, aid traders and miners, support musicians, protect and encourage lovers

**Anathema** Discriminate or slight someone based on appearance, intentionally disfigure a creature, refuse food to the starving

**Religious Symbol** solar disk with horns

**Sacred Animal** cow

**Sacred Colors** yellow, red

**Source:** `= this.source` (`= this.source-type`)
