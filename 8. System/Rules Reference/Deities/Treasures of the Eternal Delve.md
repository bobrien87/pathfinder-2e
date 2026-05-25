---
type: deity
source-type: "Remaster"
domains: "Earth, Might, Toil, Wealth"
favored-weapon: "Pick"
divine-font: "Harm, Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Pummeling Rubble]], Rank 3: [[Earthbind]], Rank 8: [[Earthquake]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The endless tunnels and caverns of the Plane of Earth host a multitude of burrowing creatures, beings made of stone, and those who continually excavate precious gems from the surrounding rock. This near-ceaseless labor generates a kind of divine power that those who respect the soil can give their faith to, in the form of this covenant. They appreciate the dichotomy between the sheer strength of stone and the sometimes delicate nature of crystals and gems, and the fact that the latter is often more valuable than the former. But these worshippers know that all things that come from the earth have their own beauty. Followers of the Treasures of the Eternal Delve also respect the importance of stability and safety when searching for these riches, as many of them could be easily crushed by a collapsing tunnel or falling slab of rock.

**Covenant Members** earth elementals, jabalis, the Plane of Earth, spirits of earth, xiomorn vault builders

**Areas of Concern** burrowing, gemstones, soil, stability, stones

**Edicts** appreciate the beauty of all stones, safely mine for ore, walk barefoot across soil or stones when possible

**Anathema** purposefully cause a cave-in, shatter a precious gem

**Religious Symbol** rolling boulder

**Source:** `= this.source` (`= this.source-type`)
