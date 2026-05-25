---
type: deity
source-type: "Remaster"
domains: "Ambition, Confidence, Passion, Water"
favored-weapon: "Trident"
divine-font: "Harm, Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Tailwind]], Rank 3: [[Aqueous Orb]], Rank 4: [[Hydraulic Torrent]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

From Obari's earliest days as a member of a pantheon of ocean gods, he sought to travel beyond the bounds of the water, journeying to distant lands in search of something to give him a sense of purpose. His one constant during these travels was the goddess Vudravati, whom he courted with elaborate stories of their potential future together, delighting her even as she also grew closer to his twin brother Embaral. When she sought to take both as lovers, Obari and Embaral became consumed by jealousy and began warring with each other over Vudravati's affections.

The fervor of the conflict between Obari and Embaral ultimately led to the loss of Golarion's other gods of the ocean. Combat and voluntary self-exile eroded their numbers, ending only when Vudravati separated the brothers forever by laying between them in eternal slumber, creating the land of Vudra. Her children are said to be the Vudrani people.

**Title** The Wandering Storm

**Areas of Concern** exploration, forbidden love, wanderlust

**Edicts** face unfamiliar challenges, travel to new places and seek new experiences, pursue dangerous or forbidden relationships

**Anathema** abandon a sworn lover, constantly pursue safe choices, shun change

**Religious Symbol** broken anchor

**Sacred Animal** sailfish

**Sacred Colors** dark blue, dark green, gray

**Source:** `= this.source` (`= this.source-type`)
