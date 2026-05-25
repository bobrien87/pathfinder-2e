---
type: deity
source-type: "Remaster"
domains: "Destruction, Healing, Truth, Zeal"
favored-weapon: "Sickle"
divine-font: "Harm, Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Sure Strike]], Rank 3: [[Hypercognition]], Rank 6: [[Disintegrate]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Pahti Coatl (PAH-tee coh-AHtl) is a god dedicated to the removal of evil from Golarion, either in the form of salvation or destruction. Unlike her younger siblings, Pahti Coatl has a different approach with defending good and innocent people by actively seeking out and ridding evil from the world. Pahti Coatl teaches that it is easy to fall in to a path of blind destruction and that one must be assured that one's campaign is not without reasonable cause. She encourages learning about others to confirm their wrongdoings and make sure that an evil person acts so willingly and not due to circumstance. Pahti Coatl knows that a parent unable to feed their child may turn to evil acts like theft and that such straying from the path in these circumstances must be met not with vengeance, but with forgiveness and care. In these cases, she takes on the aspect of the Healer of Souls, hoping to return a straying individual to the path of righteousness.

**Title** Healer of Souls

**Areas of Concern** Investigation, rehabilitation, retribution

**Edicts** Attempt to help others return to a righteous path, seek out evils that threaten innocents, learn what you can about evil doers and the reasons for their actions

**Anathema** Refuse to outright destroy an overwhelming evil, strike down another without proving that they have done wrong, reject someone honestly seeking redemption

**Religious Symbol** coatl feather wreathed in flame

**Sacred Animal** hummingbird

**Sacred Colors** lavender

**Source:** `= this.source` (`= this.source-type`)
