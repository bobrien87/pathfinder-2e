---
type: deity
source-type: "Remaster"
domains: "Air, Decay, Plague, Swarm"
favored-weapon: "Spear"
divine-font: "Harm"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Goblin Pox]], Rank 2: [[Vomit Swarm]], Rank 3: [[Insect Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Ghlaunder is the god of pestilence, infection, and insects. His form resembles that of a giant mosquito, warped and distended by the parasites he hosts. He leaves malaise in his wake, laying waste to everything he can. Ghlaunder revels in suffering, especially that caused by sickness: the last gasp of air into fluid-filled lungs, the terrorizing dreams that come only from the hottest of fevers. It is said that the Gossamer King was once swaddled in a cocoon, but was released by the curious Desna into the world with a cleave of her starknife. Since then, the goddess has pursued him in a macabre dance, hoping to kill him as they flit between planes.

**Title** The Gossamer King

**Areas of Concern** infection, insects, parasites, stagnation

**Edicts** corrupt pieces of land, water sources, and communities; infest the weak; spread and nurture disease

**Anathema** aid in ending a plague or infection, destroy something out of hand when you could have instead corrupted it or leeched off it first

**Religious Symbol** mosquito in profile

**Sacred Animal** mosquito

**Sacred Color** light gray, red

**Source:** `= this.source` (`= this.source-type`)
