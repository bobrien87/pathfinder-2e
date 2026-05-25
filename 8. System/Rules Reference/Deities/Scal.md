---
type: deity
source-type: "Remaster"
domains: "Destruction, Earth, Freedom, Perfection"
favored-weapon: "Meteor-hammer"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Liberating Command]], Rank 4: [[Weapon Storm]], Rank 6: [[Phantasmal Calamity]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The people of ancient Azlant worshipped Scal as the deity of catharsis and purity. His promotion of these values, however, was more violent in nature. The Calm After the Storm believed righteousness could only be found by harnessing one's own darkness to destroy anything that threatened one's existence. His teachings were not about suppressing one's inner rage, hiding it, or blocking it out, but rather using that inherent violence as a powerful weapon.

**Title** Calm after the Storm

**Areas of Concern** Annihilation, catharsis, purity

**Edicts** Strive for physical and mental perfection, tap into one's inner darkness to destroy anything that compromises one's pursuit of righteous perfection, take vengeance when necessary

**Anathema** Indulge in gluttonous or lazy behavior, give up without a fight, refuse a duel

**Religious Symbol** burning meteor impacting the ground

**Sacred Animal** wolverine

**Sacred Colors** red

**Source:** `= this.source` (`= this.source-type`)
