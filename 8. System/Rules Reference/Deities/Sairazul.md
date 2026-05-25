---
type: deity
source-type: "Remaster"
domains: "Earth, Family, Toil, Wealth"
favored-weapon: "Pick"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Shattering Gem]], Rank 2: [[Expeditious Excavation]], Rank 4: [[Mountain Resilience]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Sairazul, the Crystalline Queen, is the elemental lord of caves, earth, and gems. Planar scholars who know of the benevolent lord of earth speak of Sairazul as a mother and creator who gave birth to numerous planar creatures, including agrawghs and crysmals. Though many of her progeny were stolen away from her while she was imprisoned, her return has heralded widespread worship on the Plane of Earth, and even among mortal cultists who exalt creation and reproduction.

**Title** The Crystalline Queen

**Areas of Concern** Bounties of the earth, caves, fertility, gems

**Edicts** Aid childbirths, care for Sairazul's children, mine responsibly, shelter others within stone and earth

**Anathema** Collapse an earthen structure on a creature, damage subterranean natural wonders

**Religious Symbol** yellow gem with geode eye

**Sacred Animal** ant

**Sacred Colors** amber, green

**Source:** `= this.source` (`= this.source-type`)
