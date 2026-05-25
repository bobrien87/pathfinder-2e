---
type: deity
source-type: "Remaster"
domains: "Knowledge, Travel, Trickery, Wealth"
favored-weapon: "Sickle"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Befuddle]], Rank 4: [[Translocate]], Rank 6: [[Never Mind]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Areshkagal, the Faceless Sphinx, is the demon lord of greed, portals of all kinds, and inscrutable riddles. While in decline due to the loss of her territory to her half-sister Aldinach, this demon lord still has formidable power and wealth, although her real strength lies in her abilities of deception, sequestering treasures behind riddle locks and portal traps. She appears as a faceless, six-legged sphinx with blue fur and pale, ashen skin. Her wings resemble those of a dragon and her tail is a viper that hisses her countless unfair riddles. Her cultists, usually based near deserts, remain equally enigmatic with their own puzzles, veiled coded language, and seething rage at their diminishing numbers. Because of Areshkagal's secretive nature, followers often form mystery cults, with layers upon layers of falsehoods so intricate that initiates often don't realize they follow the Faceless Sphinx.

**Title** The Faceless Sphinx

**Areas of Concern** Greed, knowledge, portals, riddles

**Edicts** Clear paths and portals, develop new riddles, hide your intentions

**Anathema** Reveal knowledge without personal gain, show mercy to cultists of Aldinach, willingly relinquish wealth

**Religious Symbol** faceless female pharaoh

**Sacred Animal** viper

**Sacred Colors** blue, gold

**Source:** `= this.source` (`= this.source-type`)
