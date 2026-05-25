---
type: deity
source-type: "Remaster"
domains: "Ambition, Confidence, Might, Zeal"
favored-weapon: "Maul"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Ant Haul]], Rank 2: [[Enlarge]], Rank 4: [[Mountain Resilience]]"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Brother Bold

**Areas of Concern** Boasts, bravery, strength

**Edicts** Participate in feats of strength, rally the fearful to fight, proclaim your prowess in colorful ways

**Anathema** Be the first to flee a fight, mock someone for being weak, accuse another's boasting of lies without proof

**Religious Symbol** Open palm glowing with gold light

**Sacred Animal** Leopard

**Sacred Colors** Bronze, gold

**Source:** `= this.source` (`= this.source-type`)
