---
type: deity
source-type: "Remaster"
domains: "Change, Decay, Knowledge, Metal"
favored-weapon: "Warhammer"
divine-font: "Harm"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Fold Metal]], Rank 5: [[Impaling Spike]], Rank 8: [[Ferrous Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Though the Plane of Metal has only recently returned to the planar cosmology, it has garnered a fair share of divine interest. The chaotic plane of rusting cityscapes and seas of ferromagnetic liquids has equally changeable inhabitants, many of whom have fluid forms. As such, alchemy is an important aspect of the plane and the followers of the Shapes of the Fading Luster, who constantly seek innovate ways to work with metal. As part of their faith, they seek to be on the forefront of progress. However, they also understand that certain types of decay (such as rust or the half-life of a radioactive isotope) are natural processes that should be respected when they are unavoidable. Of course, these worshippers aren't about to neglect an item made from a precious metal without reason. After all, a bit of polish and a few minutes of work will help make it look as good as new!

**Covenant Members** capritellixes, metal elementals, the Plane of Metal, spirits of metal, zuhras

**Areas of Concern** alchemy, base metals, precious metals, progress, rust

**Edicts** craft with metal, either allow a piece of metal to rust away or continually keep it polished, learn the highest secrets of alchemy

**Anathema** destroy metallic objects quickly instead of letting them rust away, purposefully transform a precious metal into a base metal

**Religious Symbol** drop of liquid metal

**Source:** `= this.source` (`= this.source-type`)
