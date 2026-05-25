---
type: deity
source-type: "Remaster"
domains: "Duty, Knowledge, Luck, Star"
favored-weapon: "Dueling-pistol"
divine-font: "Harm, Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Sure Strike]], Rank 4: [[Clairvoyance]], Rank 7: [[True Target]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Tales of gunslingers and magical firearms are common throughout the lands of Arcadia. The most notable of these weapons are the star guns, firearms capable of firing magical energy that flows with the light of the stars. Although knowledge of the creation of star guns has been lost, stories of their origin all point to the Crowned Regents, a mysterious people that inhabited the Crownpeaks of Arcadia.

Legends of the Crowned Regents disagree with one another or outright contradict themselves, but one of the few constants across the stories is a figure named Kaldemash. The tales note that wise Kaldemash was there when the first star guns were forged and was quick to realize the dangerous potential of the new weapons. He retreated to his chambers, toiled for ten days, and emerged with the Star Code, a list of rules on the appropriate use of star guns and behavior of anyone carrying such a weapon. It's unclear if the establishment of the code was the cause for Kaldemash's divine ascension, but once he reached divinity, the Star Code spread beyond the Crownpeaks and has remained a staple of the Deadshot Lands and greater Arcadia ever since. With increased trade between Arcadia and the Mwangi Expanse, the Star Code and Kaldemash's teachings have even begun to spread throughout the Inner Sea region.

**Title** Keeper of the Code

**Areas of Concern** birds of prey, firearms, and honorable combat

**Edicts** let others know your grievances, offer a just duel to those who seek satisfaction, uphold the Star Code, use your firearm in a safe manner

**Anathema** break the terms of a duel, harm innocents or anyone not involved with your duel or grievances, willingly provide a firearm to a reckless person

**Religious Symbol** talon clutching a bullet made of starlight

**Sacred Animal** falcon

**Sacred Colors** gray, red

**Source:** `= this.source` (`= this.source-type`)
