---
type: deity
source-type: "Remaster"
domains: "Ambition, Death, Pain, Trickery"
favored-weapon: "Dagger"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Phantom Pain]], Rank 2: [[Invisibility]], Rank 3: [[Haste]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Shax, the Blood Marquis, is the demon lord of envy, lies, and sadistic murders. Shax's capacity for cruelty is legendary even among the ranks of demon lords, and he takes extreme pleasure in watching the last light of hope fade from the eyes of his victims. He is also known for creating demons, and those whom he personally flays and corrupts with chthonian influence remain exemplars of their kind. Shax appears as a human man with a dove's head, feet, and wings, carrying countless knives and other weapons all over his body. Shax is most frequently worshipped by sadists, lone murderers, and serial killers.

**Title** The Blood Marquis

**Areas of Concern** Envy, lies, murder

**Edicts** Plot and commit murders, tell lies, torture creatures

**Anathema** Sleep in a building with fewer than five rooms, allow a victim to escape due to gloating

**Religious Symbol** white bloody feather

**Sacred Animal** stork

**Sacred Colors** red, white

**Source:** `= this.source` (`= this.source-type`)
