---
type: deity
source-type: "Remaster"
domains: "Death, Duty, Pain, Trickery"
favored-weapon: "Shuriken"
divine-font: "Harm"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Sure Strike]], Rank 2: [[Invisibility]], Rank 6: [[Mislead]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Minister of Blood

**Areas of Concern** Harsh justice, murder, punishment

**Edicts** Commit assassinations for hire, strike unseen, carry out punishment for convicted criminals

**Anathema** Show mercy to a target, take credit for your assassinations, refuse to punish a lawfully convicted criminal, slaughter indiscriminately

**Religious Symbol** shuriken drenched in blood

**Sacred Animal** tiger

**Sacred Colors** black, white

**Source:** `= this.source` (`= this.source-type`)
