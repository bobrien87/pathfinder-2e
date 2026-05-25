---
type: deity
source-type: "Remaster"
domains: "Family, Freedom, Healing, Vigil"
favored-weapon: "Longsword"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Phantasmal Minion]], Rank 3: [[Cozy Cabin]], Rank 5: [[Telekinetic Haul]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

While some deities advance an agenda of civilization seemingly no matter the costs, the benefactors of this covenant want such large collections of mortals to support one another. Communities thrive when they work together for a greater good that transcends concepts like zoning laws and gentrified neighborhoods. Followers of the Good Neighbors appreciate families (both blood kin and found families) and unity, though not at the sacrifice of individual freedom. They strive to make their neighborhoods better places by repairing damaged structures, keeping shared spaces neat and tidy, and aiding those who might have fallen through the cracks of society. Adherents to this covenant might remain within a single settlement or travel from location to location, bringing their practicality and optimism to cities and towns in need.

**Covenant Members** Cayden Cailean, Erastil, household spirits, Sarenrae, Torag

**Areas of Concern** community service, compassion, liberty, solidarity

**Edicts** participate in the betterment of your community, provide aid after disasters damage settlements, volunteer your time and resources for good causes

**Anathema** allow a community space to fall into disrepair, dictate where and how people should live

**Religious Symbol** broom resting on a hearth

**Source:** `= this.source` (`= this.source-type`)
