---
type: deity
source-type: "Remaster"
domains: "Healing, Magic, Nature, Protection"
favored-weapon: "Whip"
divine-font: "Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Soothe]], Rank 2: [[Vomit Swarm]], Rank 3: [[Paralyze]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Mistress of the Beautiful House

**Areas of Concern** Embalming, healing, scorpions

**Edicts** Avenge the wronged, protect the dead and the vulnerable, use poison and suffocation, heal others

**Anathema** Poison someone you didn't intend to, harm a creature as punishment for a different creature's crime, desecrate a corpse

**Religious Symbol** red scorpion

**Sacred Animal** scorpion

**Sacred Colors** black, red

**Source:** `= this.source` (`= this.source-type`)
