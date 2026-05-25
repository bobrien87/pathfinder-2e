---
type: deity
source-type: "Remaster"
domains: "Delirium, Freedom, Knowledge, Perfection"
favored-weapon: "Hatchet"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Mindlink]], Rank 4: [[Confusion]], Rank 5: [[Synesthesia]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Called the Crownless and the Maker of Kings, Narriseminek often appears as a protean with a scar around their pate, as if left by a burning crown. Their true form, though similar, is rarely seen: an iridescent and golden protean with a halo of burning eyes but empty eye sockets. The protean lord of ascendance, keketars, and revelations rarely interacts with nonproteans, but to their protean worshippers, they offer exalted transformations and revelations that can change a being's entire outlook. Worshippers of Narriseminek, both mortal and protean, spend their time divining the future and using magic to transform their bodies—a practice they also extend to any other willing creatures that ask. Their revelations take the form of patterns emerging in otherwise random events; Narriseminek's followers reject astrology and other forms of divination based on predictable cycles.

**Title** The Crownless, the Maker of Kings

**Areas of Concern** Ascendance, keketars, revelations

**Edicts** Divine the future, transform the bodies of willing creatures, rebel against organized structures

**Anathema** Refuse to speak to a keketar, eschew a challenge by turning down a promotion or an advancement

**Religious Symbol** imentesh head wreathed in a circle of flame

**Sacred Animal** mantis shrimp

**Sacred Colors** cyan, gold

**Source:** `= this.source` (`= this.source-type`)
