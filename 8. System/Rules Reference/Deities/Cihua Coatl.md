---
type: deity
source-type: "Remaster"
domains: "Healing, Might, Protection, Zeal"
favored-weapon: "Spear"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Sure Strike]], Rank 4: [[Mountain Resilience]], Rank 7: [[True Target]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Cihua Coatl (SEE-wah coh-AHtl) is a dualistic coatl god. They support all those who defend others in the name of righteous causes. Their typical appearance is that of two coatls sharing a single body. One of these is a tletli coatl, powerful coatls known for their destructive might and righteous fury, while the other is a chicome coatl, coatls known for their ability to restore nature in areas that have been ravaged by evil. While Cihua Coatl has two distinct heads and tails, they share a pair of arms, with one holding a spear and the other a shield. Cihua Coatl teaches that conflict is inevitable, and one must be ready to defend others when such conflicts arise. The spear and shield represent the dualistic aspects of these teachings. The spear is the symbol of might: one can fight back in times of conflict, standing between aggressors and the innocent. The shield is the symbol of protection: caring for others is something that occurs at all times, not just during conflict. A follower can help others by offering services and kindness to their community.

**Title** The War Children

**Areas of Concern** Childbirth, protection, warfare

**Edicts** Aid in the rearing of children; prepare your body, mind, and community for eventual conflict; support your community

**Anathema** Engage in mindless war, refuse to answer a genuine plea for protection

**Religious Symbol** two coatls consuming each other's tails with their wings overlapping in the center

**Sacred Animal** armadillo

**Sacred Colors** gold

**Source:** `= this.source` (`= this.source-type`)
