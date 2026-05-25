---
type: deity
source-type: "Remaster"
domains: "Darkness, Fate, Freedom, Moon"
favored-weapon: "Starknife"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Penumbral Shroud]], Rank 4: [[Translocate]], Rank 9: [[Falling Stars]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Cosmic Caravan is known to astronomers and astrologers alike as a collection of constellations in the sky, said to travel forever in a circle around the star Cynosure. The association of a diverse array of gods and demigods thematically linked with the stars and the spaces between is a relatively new faith that first rose to prominence in western Avistan, particularly in Varisia, Nidal, and Ravounel. The deities worshiped by the faithful of the Cosmic Caravan include: Desna, Groetus, and Sarenrae; the empyreal lords Ashava, Black Butterfly, and Pulura; the elven god Ketephys; and the outer god Yog-Sothoth. This faith has been gaining ground particularly in Nidal, where the worship of the night is overwhelmingly associated with Zon-Kuthon, and a rising number of Cosmic Caravan worshipers seek to oppose or, one day, even overthrow the Midnight Lord's theocracy to reclaim the night from the implications that all who dwell in the dark are evil.

**Pantheon Members** Ashava, Black Butterfly, Desna, Ketephys, Pulura, Sarenrae, Tsukiyo, Yog-Sothoth

**Areas of Concern** constellations, hope for a better tomorrow, fortune telling, the night

**Edicts** aid those who live in regions where Zon-Kuthon (or other religions that espouse the night as a bastion for evil) holds sway, help the desperate or forlorn to see potential for a better life in the future, spend time stargazing or meditating in moonlight, travel with no particular destination in mind

**Anathema** destroy astronomical or astrological equipment, portray the night as a time of evil, spend the night in the place twice in a row (such as the same room in an inn or the same natural clearing)

**Religious Symbol** wagon-shaped constellation

**Source:** `= this.source` (`= this.source-type`)
