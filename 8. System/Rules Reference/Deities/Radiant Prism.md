---
type: deity
source-type: "Remaster"
domains: "Creation, Moon, Protection, Sun"
favored-weapon: "Shortsword"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Sleep]], Rank 3: [[Fireball]], Rank 4: [[Creation]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The shining sun of Sarenrae, the twinkling stars of Desna, and the shimmering rainbow of Shelyn come together to form the Radiant Prism, a relatively small pantheon worshipped by those who actively fight against evil to protect the innocent. These three goddesses have been romantically involved with one another from time to time, so it makes sense that they would form a coalition. In addition to defeating the wicked, the Radiant Prism promotes the creation of beautiful works of art to bring more grace to the world.

**Pantheon Members** Desna, Sarenrae, Shelyn

**Edicts** create works that inspire good acts, defend those who cannot defend themselves, pursue evil

**Anathema** allow evil to spread, destroy that which brings joy to others, fail to offer evil a chance to surrender

**Religious Symbol** rainbow arcing between the sun and a twinkling star

**Source:** `= this.source` (`= this.source-type`)
