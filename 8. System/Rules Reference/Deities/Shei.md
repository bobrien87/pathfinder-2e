---
type: deity
source-type: "Remaster"
domains: "Family, Freedom, Healing, Perfection"
favored-weapon: "Sickle"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Liberating Command]], Rank 3: [[Hypercognition]], Rank 5: [[Dreaming Potential]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Ibis Matron

**Areas of Concern** Age, life, self-actualization

**Edicts** Empower local communities, learn from elders, share and teach from experiences

**Anathema** Force others to follow your path, inflict void damage, age others or steal life with magic

**Religious Symbol** vine-wrapped sickle

**Sacred Animal** dragonfly

**Sacred Colors** green, silver

**Source:** `= this.source` (`= this.source-type`)
