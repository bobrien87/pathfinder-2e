---
type: deity
source-type: "Remaster"
domains: "Fate, Secrecy, Trickery, Truth"
favored-weapon: "Light-mace"
divine-font: "Harm, Heal"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Anticipate Peril]], Rank 2: [[Invisibility]], Rank 5: [[Subconscious Suggestion]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Erecura is the queen of Dis, second layer of Hell, and the wife of its ruler, the archdevil Dispater. Despite being an authority figure in Hell, her outlook and motivation are far removed from that of devils, and unclear to even her own husband.

**Title** Queen of Dis

**Areas of Concern** Deduction, mind reading, subtlety

**Edicts** Manipulate dangerous beings and opportunities to your benefit, thrive in hostile conditions, divine the future

**Anathema** Despoil nature, kill a natural plant or animal that has managed to thrive outside of its intended environment

**Religious Symbol** halo of runes

**Sacred Animal** deer

**Sacred Colors** green, tan

**Source:** `= this.source` (`= this.source-type`)
