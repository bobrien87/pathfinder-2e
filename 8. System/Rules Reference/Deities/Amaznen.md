---
type: deity
source-type: "Remaster"
domains: "Creation, Knowledge, Magic, Protection"
favored-weapon: "Light-hammer"
divine-font: "Harm, Heal"
divine-skill: "Arcana"
divine-spells: "Rank 1: [[Temporary Tool]], Rank 6: [[Tree Of Seasons]], Rank 7: [[Retrocognition]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Amaznen, the Father of Invention, was the Azlanti god of invention, magic and secret knowledge. Like Aesocar, he taught his followers to utilize both divine power and the power of science and technology. Amaznen focused more on inventing constructs to ease the burden of daily life, rather than the science of healing. The Father of Invention is most remembered for the role he played during the events of Earthfall. After his lover, Acavna, lost her life attempting to subvert the meteor, Amaznen absorbed the remaining magic of the incoming debris. It is unclear whether he died, or simply disappeared from existence after Acavna's death.

**Title** The Father of Invention

**Areas of Concern** Invention, magic, secret knowledge

**Edicts** Constantly pursue new knowledge; hold secrets close to the chest; prioritize discovery, invention, and innovation through fusion of magic and technology

**Anathema** Share knowledge too freely, throw something away that could be repurposed, take credit for another's invention or idea

**Religious Symbol** gears that resemble an eye

**Sacred Animal** bee

**Sacred Colors** silver

**Source:** `= this.source` (`= this.source-type`)
